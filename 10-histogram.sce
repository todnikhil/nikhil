clc;
clear all;
a=imread('lena.jpeg');
a=rgb2gray(a);
h=zeros(1,258);
[r,c]=size(a);
for i=1:r
    for j=1:c
        if (a(i,j)==0)
            h(0)=h(0)+1;
        end
        k=a(i,j);
        h(k)=h(k)+1;
    end
end
figure(1);
subplot(1,2,1);
imshow(uint8(a));
title('Original Image')
subplot(1,2,2);
bar(h);
title('Image histogram');

