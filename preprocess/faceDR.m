
clear;clc
load('G:/PR/data/faceDR_gai.mat');
faceDR_chuli = zeros(2000,5);
j = 1222;
for i = 1:2000
    faceDR_chuli(i,1) = i+j;
    if faceDRgai(i,2) == 'mail'
        faceDR_chuli(i,2) = 1;
    elseif faceDRgai(i,2) == 'female'
        faceDR_chuli(i,2) = 0;
    elseif faceDRgai(i,2) == 'descriptor'
        faceDR_chuli(i,2) = -1;
    end
    
    if faceDRgai(i,3) == 'child'
        faceDR_chuli(i,3) = 1;
    elseif faceDRgai(i,3) == 'teen'
        faceDR_chuli(i,3) = 2;
    elseif faceDRgai(i,3) == 'adult'
        faceDR_chuli(i,3) = 3;
    elseif faceDRgai(i,3) == 'senior'
        faceDR_chuli(i,3) = 4;
    else
        faceDR_chuli(i,3) = -1;
    end
    
    if faceDRgai(i,4) == 'black'
        faceDR_chuli(i,4) = 1;
    elseif faceDRgai(i,4) == 'white'
        faceDR_chuli(i,4) = 2;
    elseif faceDRgai(i,4) == 'asian'
        faceDR_chuli(i,4) = 3;
    elseif faceDRgai(i,4) == 'hispanic'
        faceDR_chuli(i,4) = 4;
    elseif faceDRgai(i,4) == 'other'
        faceDR_chuli(i,4) = 5;
    else
        faceDR_chuli(i,4) = -1;
    end
    
    if faceDRgai(i,5) == 'smiling'
        faceDR_chuli(i,5) = 1;
    elseif faceDRgai(i,5) == 'serious'
        faceDR_chuli(i,5) = 2;
    elseif faceDRgai(i,5) == 'funny'
        faceDR_chuli(i,5) = 3;
    else
        faceDR_chuli(i,5) = -1;
    end
    
end

xlswrite('G:/PR/data/faceDR_fin.xls',faceDR_chuli);
