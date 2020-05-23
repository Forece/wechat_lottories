import requests


def main():
    url = "https://lucky.nocode.com/v2/lottery/public"
    headers = {
        # 请修改为自己的 Authorization
        "Authorization": ""}  # 引号内填写
    res = requests.get(url, headers=headers)
    public_info = res.json()['public']
    square_info = res.json()['square']
    for p_id in public_info:
        p_url = 'https://lucky.nocode.com/v2/lottery/%s/join' % p_id['id']
        res = requests.post(p_url, headers=headers)
        data = res.json()
        if res.status_code == 200 and 'errors' not in data:
            print("成功参与抽奖：《%s》" % (p_id['prizes']['data'][0]['name']))
        else:
            print("Whoops, Something Happened")
    for s_id in square_info:
        p_url = 'https://lucky.nocode.com/v2/lottery/%s/join' % s_id['id']
        res = requests.post(p_url, headers=headers)
        data = res.json()
        if res.status_code == 200 and 'errors' not in data:
            print("成功参与抽奖：《%s》" % (s_id['prizes']['data'][0]['name']))
        else:
            print("Whoops, Something Happened")


if __name__ == '__main__':
    main()
