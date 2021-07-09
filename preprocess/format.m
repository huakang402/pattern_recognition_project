%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% It is a matlab .m file to change photo format to .jpg %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

missing_data = [];
for i = 1223:5222
   ch = int2str(i);
   fid=fopen(strcat('../data/rawdata/', ch));
   if(fid ~= -1)
       I = fread(fid);
       h = imagesc(reshape(I, 128, 128)');
       if(i == 2412 || i == 2416)
           h = imagesc(reshape(I, 512, 512)');
       end
       map = colormap(gray(256));
       saveas(h, strcat('../data/jpg/', ch, '.jpg'));
       fclose(fid);
   end
   if (fid == -1)
       missing_data = [missing_data,i];
   end
end
xlswrite('missing_data.xls',missing_data);