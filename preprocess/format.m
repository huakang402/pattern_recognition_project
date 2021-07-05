%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% It is a matlab .m file to change photo format to .jpg %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for i = 1223:5222
   ch = int2str(i);
   fid=fopen(strcat('../data/rawdata/', ch));
   if(fid ~= -1)
       I = fread(fid);
       h = imagesc(reshape(I, 128, 128)');
       map = colormap(gray(256));
       saveas(h, strcat('../data/jpg/', ch, '.jpg'));
       fclose(fid);
   end
end
