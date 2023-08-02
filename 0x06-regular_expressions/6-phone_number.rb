#!/usr/bin/env ruby
# match a ten digit number

puts ARGV[0].scan(/^[0-9]{10}$/).join
