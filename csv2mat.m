% Converts CSV to double for MATLAB Manipulation and removal of duplicate
% users

importfile('B:/Twitter/topusers.csv')

b = cat(1,topusers(:));
b = sort(b,2);
b = unique(b,'rows');
b = flipud(b);
clear topusers;

% Write the data back out as a CSV file
csvwrite('B:/Twitter/topusers_clean.csv')