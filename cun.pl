#!/usr/bin/perl
#Simple Currency Converter Using xe.com
use LWP::UserAgent;

#Let's clear our terminal for fresh use.
my $sys="$^O";if ($sys eq 'MSWin32') { system("cls"); } else { system("clear"); }

#Here we check to be sure we're on point. Then we commence with work.
if (length(<@ARGV>) < 3)
{
print "Example: $0 1000 USD to EUR\n";
}else{
print "Am fine\n";
my $amount = @ARGV[0];
my $from = @ARGV[1];
my $to = @ARGV[2];
my $ua = LWP::UserAgent->new();
$ua->agent( "Mozilla/5.0 (X11; Linux i686; rv:2.0.0) Gecko/20100101" );
my $contents = $ua->get("http://www.xe.com/currencyconverter/convert/?Amount=$amount&From=$from&To=".$to);
if ( $contents->is_success )
{
my $resp = $contents->content;
if($resp =~ m/<td width="47%" align="right" class="leftCol">(.+)/ig)
{
my $amt = $1;
if($resp =~ m/<td width="47%" align="left" class="rightCol">(.+)\&nbsp/ig)
{
my $amtreturn = $1;
print "Xchange: $amount $from to $to is $amtreturn";
}
}else{
print "Xchange: No result found!\nTry $0 1000 USD to EUR";
    }
  }
}
