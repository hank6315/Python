from multiprocessing import Pool


def send_mail(username, coupon_code, extra_sentence):
    print(username, coupon_code, extra_sentence or '')


def main():
    with Pool(4) as pool:
        for idx in range(1, 100):
            pool.apply_async(
                send_mail,
                (f'user{idx:0>2}', f'vipcode{idx:0>2}'),
                {'extra_sentence': f'{idx:0>4}'}
            )
        pool.close()
        pool.join()



if __name__ == '__main__':
    main()