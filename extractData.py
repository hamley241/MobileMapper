import time
import redis


def make_dictionary(filename = '''/Users/patley/Hike/Dynamic Rewards/Circles_mobile.csv'''):
    f = open(filename,'r')
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    ## I d in row1, data starts from 6 and ends at -1
    mapping_dict = {}
    count = 4
    for line in f:
        count += 1
        print count
        print line,
        rows_data = line
        rows_data = rows_data.rstrip('\r\n')
        rows_data = rows_data.rstrip(',')
        split_row = rows_data.split(',') ## This containd data

        if split_row[1] in mapping_dict.keys():
            mapping_dict[split_row[1]] = mapping_dict[split_row[1]] + split_row[5:]

        else:
            mapping_dict[split_row[1]] = split_row[5:-1]

        print mapping_dict[split_row[1]]
        #time.sleep(1)
    print mapping_dict.keys()[0]+ " "+str(mapping_dict[mapping_dict.keys()[0]])
    return mapping_dict

def make_redis_comaptible(mapp):
    ## Converting dictionary into relevant data strcuture

    #r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(host='10.0.1.241', port=6379, db=0)
    global phmap_key
    new_m = {}
    for item in mapp.keys():
        print 'It is '+item
        for valu in mapp[item]:
            new_m[valu] = item
            r.hset(phmap_key,valu, new_m[valu])
            #print 'insertion is '+new_m[valu]+  ' key is '+ valu
    return new_m

def get_locality(numb, mapp):
    if numb[:5] in mapp.keys():
        print 'User location at ' + str(mapp[numb[:5]])
    elif numb[:4] in mapp.keys():
        print 'User found at ' + str(mapp[numb[:4]])
    else:
        print 'User not found'

    # while i<10:
    #     if str(qur[0:i]) in kil.keys() and str(qur[0:i+1]) not in kil.keys():
    #         print str(kil[qur[0:i]])
    #     i = i+1
    # # else:
    # #     print 'not Found'

if __name__ == '__main__':
    filename = '''/Users/patley/Hike/Dynamic Rewards/Circles_mobile.csv'''
    phmap_key = 'phmp'
    sampl = make_dictionary(filename)
    print "zones: "+str(len(sampl))

    mapp = make_redis_comaptible(sampl)
    print '#####Done'
    #get_locality('85157',mapp)


#######

#redis.


"""
mapping_dict = {}
#for line in f:
rows_data = f.readline()
rows_data = rows_data.rstrip('\r\n')
rows_data = rows_data.rstrip(',')
split_row = rows_data.split(',')
if split_row[1] in mapping_dict.keys():
    mapping_dict[split_row[1]] = mapping_dict[split_row[1]] + split_row[6:-1]
else:
    mapping_dict[split_row[1]] = split_row[6:-1]




"""
"""
f = open(filename,'r')
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    ## I d in row1, data starts from 6 and ends at -1
    mapping_dict = {}
    count = 4
    for line in f:
        count = count +1
        print count
        print line,
        rows_data = line
        rows_data = rows_data.rstrip('\r\n')
        rows_data = rows_data.rstrip(',')
        split_row = rows_data.split(',')

        if split_row[1] in mapping_dict.keys():
            mapping_dict[split_row[1]] = mapping_dict[split_row[1]] + split_row[5:]
        else:
            mapping_dict[split_row[1]] = split_row[5:-1]
        print mapping_dict[split_row[1]]
        #time.sleep(1)
    print mapping_dict.keys()[0]+ " "+str(mapping_dict[mapping_dict.keys()[0]])
    #return mapping_dict
    """
