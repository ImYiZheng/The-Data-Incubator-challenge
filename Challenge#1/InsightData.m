%% find mean and std
tic
Times = 9999999;
difference = zeros(1,Times);
T = 32;    %    8 or 32
N = 4;     %    2 or 4
sum = 0;
for i=1:1:Times
    stream = unidrnd(10,1,T);
    descend = sort(stream,'descend');
    max_reg = descend(:,1:N);
    last_reg = stream(:,T-N+1:T);
    M = prod(max_reg);
    L = prod(last_reg);
    difference(1,i) = M - L;
    i
end
mean_ML = mean(difference)
std_ML = std(difference)
toc
%% find conditional probability
tic
Times = 99999999;
a = 32;     % 32 or 2048 
b = 64;     % 64 or 4096
P1 = 0;
P2 = 0;
T = 8;      % 8 or 32
N = 2;      % 2 or 4
for i=1:1:Times
    stream = unidrnd(10,1,T);
    descend = sort(stream,'descend');
    max_reg = descend(:,1:N);
    last_reg = stream(:,T-N+1:T);
    M = prod(max_reg);
    L = prod(last_reg);
    difference = M - L;
    if difference <= b
        P1 = P1 + 1;
        if difference >= a
            P2 = P2 + 1;
        end       
    end
    i
end
p1 = P2/P1;
toc