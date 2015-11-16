echo off;
 znaki(1,:) =  [1 1 1, 1 0 1, 1 0 1, 1 0 1, 1 1 1];
 znaki(2,:) =  [0 1 0, 0 1 0, 0 1 0, 0 1 0, 0 1 0];
 znaki(3,:) =  [1 1 1, 0 0 1, 1 1 1, 1 0 0, 1 1 1];
 znaki(4,:) =  [1 1 1, 0 0 1, 0 1 1, 0 0 1, 1 1 1];
 znaki(5,:) =  [1 0 1, 1 0 1, 1 1 1, 0 0 1, 0 0 1];
 znaki(6,:) =  [1 1 1, 1 0 0, 1 1 1, 0 0 1, 1 1 1];
 znaki(7,:) =  [1 1 1, 1 0 0, 1 1 1, 1 0 1, 1 1 1];
 znaki(8,:) =  [1 1 1, 0 0 1, 0 0 1, 0 0 1, 0 0 1];
 il_znakow = 8;
znakinorm = normr(znaki);
wagi_pierwsza = (znakinorm');
sprzezenia = -1 / 8;
wagi_druga = ones(8,8) * sprzezenia;
for i=1:8,
    wagi_druga(i,i) = 1;
end
wagi_druga = [wagi_druga; eye(8)];
wagi_druga = normr(wagi_druga);
wyjscia_pierwsza = zeros(1,8);
wyjscia_druga = zeros(1,8);
ilosc_powtorzen = 15; % calkowicie arbitralna, ale zapewnia zbieznosc
for znak = 1:il_znakow,
    wyjscia_pierwsza = znakinorm(znak,:)*wagi_pierwsza;
    wyjscia_druga = satlin( ([wyjscia_druga, wyjscia_pierwsza] *wagi_druga) );
    wyjscia_pierwsza = zeros(1,8);
    for licznik = 1:ilosc_powtorzen,
        wyjscia_druga = satlin(( [wyjscia_druga, wyjscia_pierwsza] *wagi_druga));
        wyjscia_druga = normr(wyjscia_druga);
    end;
    hardlim(wyjscia_druga-0.01)
    wyjscia_druga = zeros(1,8);
end;
eta = 100;
for kolejny_blad = 1:eta,
    pozycja_x = int8(rand*8+1);
    pozycja_y = int8(rand*15+1);
    znaki(pozycja_x, pozycja_y) = abs(znaki(pozycja_x, pozycja_y) - rand);
end;
znaki
znakinorm = normr(znaki);
for znak = 1:il_znakow,
    wyjscia_pierwsza = znakinorm(znak,:)*wagi_pierwsza;
    wyjscia_druga = satlin( ([wyjscia_druga, wyjscia_pierwsza] *wagi_druga) );
    wyjscia_pierwsza = zeros(1,8);
    for licznik = 1:ilosc_powtorzen,
        wyjscia_druga = satlin(( [wyjscia_druga, wyjscia_pierwsza] *wagi_druga));
        wyjscia_druga = normr(wyjscia_druga);
    end;
    hardlim(wyjscia_druga-0.01)
    wyjscia_druga = zeros(1,8);
end;
