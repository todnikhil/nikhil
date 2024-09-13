clc;
clear all;
a=imread('C:\Nikhil\image processing\image final\lena.jpeg');
a=rgb2gray(a);
subplot(2,1,1);
imshow(a);
title('org img');
T=100; //threshold value
[r,c]=size(a);
for i=1:r
    for j=1:c
        if (a(i,j)<=T)
            x(i,j)=0;
        else
            x(i,j)=255;
    end
end
end
x=uint8(x);

subplot(2,1,2);
imshow(x);
title('threshholded img');
    


