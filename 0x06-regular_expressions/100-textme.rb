#!/usr/bin/env ruby
# This script outputs: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

Format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
List = [Format[0].compact, Format[1].compact, Format[2].compact]
puts List.join(',')
