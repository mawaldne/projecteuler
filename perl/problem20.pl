use bignum;
use List::Util qw/sum/;

$factorial = 1;
$factorial *= $_ foreach 1..100;

print sum split('', $factorial);
