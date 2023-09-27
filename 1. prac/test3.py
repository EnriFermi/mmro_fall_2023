def get_new_dictionary(input_dict_name, output_dict_name):
    dt = {}
    with open(input_dict_name, encoding='UTF-8') as f:
        size = int(f.read(2))
        for line in f.readlines():
            sline = line.replace(',', '').replace('\n', '').split(' ')
            ew = sline[0]
            for dw in sline[2:]:
                if dw not in dt:
                    dt[dw] = [ew]
                else:
                    dt[dw].append(ew)

    with open(output_dict_name, 'w+') as wf:
        wf.write(str(len(dt)))
        for key in sorted(dt.keys()):
            dt[key].sort()
            wf.write("\n{0} - {1}".format(key, ", ".join(dt[key])))
