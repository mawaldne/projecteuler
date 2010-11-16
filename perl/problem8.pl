open FILE, "problem8.txt" or die $!;

my $str;
foreach (<FILE>){ chomp; $str .= $_; }

my ($i,$max) = (0,0);
until ($i+5 == length $str){
	@digits = split(//, substr($str,$i,5));
	$temp = 1;
        foreach(@digits){$temp*=int($_)};
	$max = $temp if $temp > $max;
	$i += 1;
}
print $max;
