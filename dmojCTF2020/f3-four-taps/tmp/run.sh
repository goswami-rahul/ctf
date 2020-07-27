#!/bin/sh



temp=`mktemp reflacXXXXXX`
bak=$temp-"$1".bak
cp "$1" "$bak"


metaflac --no-utf8-convert --export-tags-to=$temp.tags  "$bak"
metaflac --export-picture-to=$temp.pic "$bak"
flac --silent -d -o - "$bak" | flac -o $temp.flac -
metaflac --no-utf8-convert $temp.flac
mv $temp.flac out.flac
rm $temp.tags $temp.pic
rm $temp
