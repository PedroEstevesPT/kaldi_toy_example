# Pedro Fonseca Esteves 2020
#
# This script gets the duration of a corpus.
#

ln -s sph2pipe_bin/sph2pipe tmp_sph2pipe
tmp="${1}corpus_size_tmp/"

if [ ! -d $tmp ]; then
    mkdir $tmp;
fi

#Copies .sph files to temporary directory
for filename in ${1}*.sph; do
    cp $filename $tmp;
done

#Converts the files to wav
for filename in ${tmp}*.sph; do
    ./tmp_sph2pipe $filename -f wav ${filename%.*}.wav;
    rm $filename
done

soxi -D $tmp/*.wav | awk '{s+=$1} END {print s " seconds"} '
rm tmp_sph2pipe
rm -r $tmp
