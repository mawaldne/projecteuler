#my $n1;
#my $n2 = 1;
#my $sum = 2;
#my $evens = 2;
#while ($sum < 4000000){
#	$n1 = $n2;
#	$n2 = $sum;
	#$sum = $n1 + $n2;
	#if (!($sum % 2)){
	#	$evens += $sum;
	#}
#}

my ($num, $last) = (1,1);
my $sum = 0;
while ($num < 4000000){
	($num, $last) = ($num + $last, $num);
	$sum += $num unless $num % 2;
}
print $sum;

