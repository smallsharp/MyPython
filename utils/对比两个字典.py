def cmp_dict(src_data, dst_data):
    # print("type: '{}' != '{}'".format(type(src_data), type(dst_data)))
    # assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data, dict):
        # print("dict len: '{}' != '{}'".format(len(src_data), len(dst_data)))
        assert len(src_data) == len(dst_data), "dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for key in src_data:
            assert key in dst_data
            cmp_dict(src_data[key], dst_data[key])
    elif isinstance(src_data, list):
        assert len(src_data) == len(dst_data), "list len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        print("{} != {}".format(src_data, dst_data))
        assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)


if __name__ == "__main__":
    import operator
    print(operator.eq(1, 1))

    xx = {"111": "sss", "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    cmp_dict(xx, yy)


