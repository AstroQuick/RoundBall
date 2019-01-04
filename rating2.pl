#!/usr/bin/perl
use File::Slurp;
use Sport::Analytics::SimpleRanking;

my $stats = Sport::Analytics::SimpleRanking->new();
my $games = read_file("games.csv", array_ref => 1);

$stats->load_data( $games );
my $srs = $stats->simpleranking();
my $mov = $stats->mov();
my $sos = $stats->sos();
for (sort keys %$srs) {
    print "Team $_ has a srs of ", $srs->{$_};
    print " and a mov of ",$mov->{$_};
    print " and a sos of ",$sos->{$_},"\n";
}

