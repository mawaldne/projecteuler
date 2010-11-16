#!/usr/bin/perl -l 

use List::Util qw/reduce max/; 

open FILE, "problem8.txt" or die $!;
my $num;
foreach (<FILE>){ chomp; $num .= $_; }

print max map { reduce { $a * $b } unpack "x${_}(A)5", $num; } 0..length($num)-5 


