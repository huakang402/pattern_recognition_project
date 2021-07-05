
clear;clc
load('G:/PR/data/faceDS_gai.mat');
faceDS_chuli = zeros(2000,5);
j = 3222;
for i = 1:2000
    faceDS_chuli(i,1) = i+j;
    if faceDSgai(i,2) == 'mail'
        faceDS_chuli(i,2) = 1;
    elseif faceDSgai(i,2) == 'female'
        faceDS_chuli(i,2) = 0;
    elseif faceDSgai(i,2) == 'descriptor'
        faceDS_chuli(i,2) = -1;
    end
    
    if faceDSgai(i,3) == 'child'
        faceDS_chuli(i,3) = 1;
    elseif faceDSgai(i,3) == 'teen'
        faceDS_chuli(i,3) = 2;
    elseif faceDSgai(i,3) == 'adult'
        faceDS_chuli(i,3) = 3;
    elseif faceDSgai(i,3) == 'senior'
        faceDS_chuli(i,3) = 4;
    else
        faceDS_chuli(i,3) = -1;
    end
    
    if faceDSgai(i,4) == 'black'
        faceDS_chuli(i,4) = 1;
    elseif faceDSgai(i,4) == 'white'
        faceDS_chuli(i,4) = 2;
    elseif faceDSgai(i,4) == 'asian'
        faceDS_chuli(i,4) = 3;
    elseif faceDSgai(i,4) == 'hispanic'
        faceDS_chuli(i,4) = 4;
    elseif faceDSgai(i,4) == 'other'
        faceDS_chuli(i,4) = 5;
    else
        faceDS_chuli(i,4) = -1;
    end
    
    if faceDSgai(i,5) == 'smiling'
        faceDS_chuli(i,5) = 1;
    elseif faceDSgai(i,5) == 'serious'
        faceDS_chuli(i,5) = 2;
    elseif faceDSgai(i,5) == 'funny'
        faceDS_chuli(i,5) = 3;
    else
        faceDS_chuli(i,5) = -1;
    end
    
end

xlswrite('G:/PR/data/faceDS_fin.xls',faceDS_chuli);
