use Sport::Analytics::SimpleRanking;
my $stats = Sport::Analytics::SimpleRanking->new();
my $games = [
    "Boston,13,Atlanta, 27",
    "Dallas,17,Chicago,21",
    "Eugene,30,Fairbanks,41",
    "Atlanta,15,Chicago,3",
    "Eugene,21,Boston,24",
    "Fairbanks,17,Dallas,7",
    "Dallas,19,Atlanta,7",
    "Boston,9,Fairbanks,31",
    "Chicago,10,Eugene,30",
];
$stats->load_data( $games );
my  $srs = $stats->simpleranking( verbose => 1 );
my $mov = $stats->mov;
my $sos = $stats->sos;
for ( keys %$srs ) {
    print "Team $_ has a srs of ", $srs->{$_};
    print " and a mov of ",$mov->{$_},"\n";
}
