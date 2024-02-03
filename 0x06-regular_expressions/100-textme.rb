#!/usr/bin/env ruby
# ssender receivver flag
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
