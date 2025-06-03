from tqdm import trange
from fastecdsa.point import Point
from fastecdsa.curve import Curve
from multiprocessing import Process, Manager

def DCsubgroup(g,a,pi,p,o,start,end,l):
    gi = g*(o//pi)
    hi = a*(o//pi)
    ggi = gi
    for c in trange(start,end):
        if ggi == hi:
            l.append(c)
            return c
        if l: return None
        ggi += gi
    return -1
def ECsubgroup(g,a,pi,p,o,start,end,l):
    gi = g*(o//pi)
    hi = a*(o//pi)
    ggi = gi
    for c in range(start,end):
        if ggi == hi:
            l.append(c)
            return c
        if l: return None
        ggi += gi
    return -1

if __name__ == '__main__':
    p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
    a = 1
    b = 4
    o = 99061670249353652702595159229088680426160873357666659718134032418967620849171
    curve = Curve(
        'scurvey',
        p,
        a,
        b,
        o,
        43190960452218023575787899214023014938926631792651638044680168600989609069200,
        20971936269255296908588589778128791635639992476076894152303569022736123671173,
    )
    G = Point(43190960452218023575787899214023014938926631792651638044680168600989609069200, 20971936269255296908588589778128791635639992476076894152303569022736123671173, curve=curve)
    A = Point(87360200456784002948566700858113190957688355783112995047798140117594305287669, 39468204126340205940090305516099025224711579213919884247902424042354015852498, curve=curve)
    B = Point(6082896373499126624029343293750138460137531774473450341235217699497602895121, 30001542408292755077473983737681093282698468370444116456645773959014482623271, curve=curve)
    procs = []
    m = Manager()
    l = m.list()
    n = 5221385621
    for i in range(1,10):
        start = n//10*i
        end = n//10*(i+1)
        p = Process(target=ECsubgroup, args=(G,A,n,p,o,start,end,l))
        p.start()
        procs.append(p)
    start = 0
    end = n//10
    DCsubgroup(G,A,n,p,o,start,end,l)
    for p in procs:
        p.join()
    print(l)
