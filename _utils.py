##############		functions		##############
###################################################

from _imports import *

lock_print = Lock()
lock_count = Lock()
counter_sync = 1


def count_sync(interval):
    global counter_sync
    lock_count.acquire()
    if (counter_sync % interval) == 0:
        print_asynch('{}'.format(counter_sync))
    counter_sync += 1
    lock_count.release()


def print_asynch(text):
    global lock_print
    lock_print.acquire()
    print(text)
    lock_print.release()


def display_df(df):
    if isinstance(df, pd.DataFrame):
        display(HTML(df.to_html()))
    else:
        print('{} is not a dataframe to be displayed!'.format(df.__name__))


def parallelize_df(df, func, context):
    # num_partitions = 10 * context.num_cores
    num_partitions = min(1 * context.num_cores, len(df))
    df_split = np.array_split(df, num_partitions)
    print('parallel: {} partitions with {} cores for {}'.format(num_partitions, context.num_cores, func.__name__))
    pool = Pool(min(context.num_cores, len(df)), maxtasksperchild=1)
    df = pd.concat(pool.map(func, df_split), ignore_index=True)
    pool.close()
    pool.join()
    del pool
    gc.collect()
    return df


def parallelize_df_dask(df, func, context):
    num_partitions = min(context.num_cores, len(df))
    # df=copy.deepcopy(df_input)
    df = dd.from_pandas(df, npartitions=num_partitions)
    print('parallel: {} partitions with {} cores for {}'.format(num_partitions, context.num_cores, func.__name__))
    return df.map_partitions(func).compute(scheduler='processes')


def init_parallel(*args, **kwds):
    pandarallel.initialize(
        progress_bar=args[0] if args[1].progress_bar_allowed else False,
        shm_size_mb=args[1].mem // args[1].num_cores if len(kwds) == 0 else kwds['size'],
        nb_workers=args[1].num_cores if len(kwds) == 0 else kwds['cores']
    )


def decode_tag_sub_v0(tag, context):
    if re.match('zzzl\w+lzzz', tag) is None:
        return tag
    tag = tag.replace('zzz', '')
    tag = tag.strip()
    # print(tag)
    nums = tag[1:-1].split('l')
    final_num = 0
    for num in nums:
        # if num in num_dict.values():
        try:
            final_num = final_num * 10 + list(context.num_dict.values()).index(num)
        except ValueError as e:
            raise Failed('{} was not in list!\n{}\n'.format(num, tag, e))
        # else:
        #     print('{} original tag, vs {} index'.format(original_tag, num))
        #     return original_tag
    return context.tags_dict[final_num]


def decode_tag_sub(tag, context):
    # if re.match('zzz\w+zzz', tag) is None:
    #     return tag
    tag = tag.replace('zzzl', ' ')
    tag = tag.replace('lzzz', ' ')
    tag = tag.strip()
    # print(tag)
    #     nums = tag[1:-1].split('l')
    words = tag.split()
    tag = words[0]
    if (len(words) > 1):
        tag = words[1]

    nums = tag.split('l')
    final_num = 0
    for num in nums:
        # if num in num_dict.values():
        try:
            final_num = final_num * 10 + list(context.num_dict.values()).index(num)
        except ValueError as e:
            raise Failed('{} was not in list!\n{}\n'.format(num, tag, e))
        # else:
        #     print('{} original tag, vs {} index'.format(original_tag, num))
        #     return original_tag
    if (len(words) == 1):
        return context.tags_dict[final_num]
    return '{} {}'.format(words[0], context.tags_dict[final_num])


def decode_tag(tag, context):
    if context.tags is None:
        return tag
    t = tag
    m = re.search('zzz(.+?)zzz', t)
    try:
        while m:
            t = t.replace(m.group(0), ' ' + decode_tag_sub(m.group(0), context) + ' ')
            m = re.search('zzz(.+?)zzz', t)
    except ValueError as e:
        print(tag)
        raise Failed('{} was wrongly coded!\n{}'.format(tag, e))
    # t = re.sub('\s+', ' ', t)
    return t.strip()


def param_setup(args, context):
    try:
        print('args = {}'.format(args))
        opts, args_l = getopt.getopt(args,
                                     "",
                                     [p + "=" for p in context.params])
    except getopt.GetoptError as e:
        print('{}\nformat: file.py {}'.format(e, ' '.join(['[--' + p + '= ]' for p in context.params])))
        sys.exit(2)
    for opt, arg in opts:
        for param in context.params:
            if opt == '--' + param:
                setattr(context, param, int(arg))
                print('{} is set to {}'.format(param, arg))


def param_setup_ipython(args, context):
    for param in context.params:
        if param in args:
            setattr(context, param, args[param])
            print('{} is set to {}'.format(param, args[param]))


class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def for_parallel(func, index_list, num_cores):
    print("Creating %i (daemon) workers and jobs in child." % num_cores)
    # pool = MyPool(min(num_cores, len(index_list)))
    pool = MyPool(num_cores)
    result = pool.map(func, index_list)
    pool.close()
    pool.join()
    del pool
    gc.collect()
    return result


def save_df_to_sql(df, save_loc, db_name, index=False):
    engine = create_engine('sqlite:///'+save_loc, echo=False)
    df.to_sql(db_name,con=engine,if_exists='replace', index=index)


class Failed(Exception):
    pass
