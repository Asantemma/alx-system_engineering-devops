#!/usr/bin/env ruby
#Accepts one arguments and pass it to a regular expression matching method

puts ARGV[0].scan(/hbtt{1,4}n/).join
