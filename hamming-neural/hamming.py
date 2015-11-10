import numpy as np
import normalize_easy
import neurolab.trans

# znaki(1,:) =  [1 1 1, 1 0 1, 1 0 1, 1 0 1, 1 1 1];
# znaki(2,:) =  [0 1 0, 0 1 0, 0 1 0, 0 1 0, 0 1 0];
# znaki(3,:) =  [1 1 1, 0 0 1, 1 1 1, 1 0 0, 1 1 1];
# znaki(4,:) =  [1 1 1, 0 0 1, 0 1 1, 0 0 1, 1 1 1];
# znaki(5,:) =  [1 0 1, 1 0 1, 1 1 1, 0 0 1, 0 0 1];
# znaki(6,:) =  [1 1 1, 1 0 0, 1 1 1, 0 0 1, 1 1 1];
# znaki(7,:) =  [1 1 1, 1 0 0, 1 1 1, 1 0 1, 1 1 1];
# znaki(8,:) =  [1 1 1, 0 0 1, 0 0 1, 0 0 1, 0 0 1];
znaki = np.ones((8, 5, 3), dtype=np.float)#10, 5, 3), dtype=np.float)

znaki[0, :] = np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]])
znaki[1, :] = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]])
znaki[2, :] = np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]])
znaki[3, :] = np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]])
znaki[4, :] = np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]])
znaki[5, :] = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]])
znaki[6, :] = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]])
znaki[7, :] = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]])
#znaki[8, :] = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]])
#znaki[9, :] = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]])

# il_znakow = 8
il_znakow = 8
#print znaki

# znakinorm = normr(znaki);
znakinorm = []
for i in znaki:
    znakinorm.append(normalize_easy.normr(i))
znakinorm = np.asarray(znakinorm)

print znakinorm

# wagi_pierwsza = (znakinorm');
wagi_pierwsza = znakinorm.conj().transpose()

# sprzezenia = -1 / 8;
sprzezenia = -1 / 8

# wagi_druga = ones(8,8) * sprzezenia;
wagi_druga = np.ones((8,8)) * sprzezenia


# for i=1:8,
#     wagi_druga(i,i) = 1;
# end
for i in xrange(0, il_znakow):
    wagi_druga[i,i] = 1

# wagi_druga = [wagi_druga; eye(8)];
wagi_druga = [wagi_druga, np.identity(8)]
wagi_druga = np.asarray(wagi_druga)

# wagi_druga = normr(wagi_druga);
a = []
for i in wagi_druga:
    a.append(normalize_easy.normr(i))
wagi_druga = np.asarray(a)

# wyjscia_pierwsza = zeros(1,8);
wyjscia_pierwsza = np.zeros((1,8))

# wyjscia_druga = zeros(1,8);
wyjscia_druga = np.zeros((1,8))

# ilosc_powtorzen = 15;
ilosc_powtorzen = 15
#print np.outer(znakinorm,wagi_pierwsza)
# for znak = 1:il_znakow,
#for i in xrange(1, il_znakow):
    # wyjscia_pierwsza = znakinorm(znak,:)*wagi_pierwsza;
    #print wagi_pierwsza.shape
    #wyjscia_pierwsza = np.outer(znakinorm[i-1,:], wagi_pierwsza)
    # wyjscia_druga = satlin( ([wyjscia_druga, wyjscia_pierwsza] *wagi_druga) );
    #satlin = neurolab.trans.SatLin()
    #wyjscia_druga = satlin(np.outer(np.asarray([wyjscia_druga,wagi_pierwsza]), wagi_druga))
#    wyjscia_pierwsza = zeros(1,8);
#    for licznik = 1:ilosc_powtorzen,
#        wyjscia_druga = satlin(( [wyjscia_druga, wyjscia_pierwsza] *wagi_druga));
#        wyjscia_druga = normr(wyjscia_druga);
#    end;
#    hardlim(wyjscia_druga-0.01)
#    wyjscia_druga = zeros(1,8);
#end;
#eta = 100;
#for kolejny_blad = 1:eta,
#    pozycja_x = int8(rand*8+1);
#    pozycja_y = int8(rand*15+1);
#    znaki(pozycja_x, pozycja_y) = abs(znaki(pozycja_x, pozycja_y) - rand);
#end;
#znaki
#znakinorm = normr(znaki);
#for znak = 1:il_znakow,
#    wyjscia_pierwsza = znakinorm(znak,:)*wagi_pierwsza;
#    wyjscia_druga = satlin( ([wyjscia_druga, wyjscia_pierwsza] *wagi_druga) );
#    wyjscia_pierwsza = zeros(1,8);
#    for licznik = 1:ilosc_powtorzen,
#        wyjscia_druga = satlin(( [wyjscia_druga, wyjscia_pierwsza] *wagi_druga));
#        wyjscia_druga = normr(wyjscia_druga);
#    end;
#    hardlim(wyjscia_druga-0.01)
#    wyjscia_druga = zeros(1,8);
#end;