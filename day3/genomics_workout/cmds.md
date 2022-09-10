# A. OBTAIN RAW DATA FROM ARCHIVE
## 1 - sratoolkit 
Visit https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit.
```shell
tar xvf sratoolkit.3.0.0-mac64.tar 
```
## 2 - configure sratoolkit
```shell
./vdb-config --interactive
./prefetch -h
```
## 3 - retrieve data by accession
```shell
prefetch SRR20334685
```
## 4 - dump fastq
```shell
fasterq-dump SRR20334685.sra 
```
## 5 - get genome fasta
```shell
wget http://ftp.ensembl.org/pub/release-107/fasta/caenorhabditis_elegans/dna/Caenorhabditis_elegans.WBcel235.dna.toplevel.fa.gz
```

# B. QC
## 1 - FASTQC 
Obtain from https://www.bioinformatics.babraham.ac.uk/projects/fastqc/.
# run analysis on fastq file
## 2 - HTSeq 
```shell
pip install HTSeq
htseq-qa -t fastq SRR20334685.fastq
```

# C. ALIGNMENT/MAPPING
## 1 - bowtie2
Visit https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.4.5/.
```shell
bowtie2 -h | head
```
## 2 - download bowtie2 BWT index or
```shell 
wget https://genome-idx.s3.amazonaws.com/bt/WBcel235.zip
```
## 2 - build your own from the genome
```shell
bowtie2-build Caenorhabditis_elegans.WBcel235.dna.toplevel.fa Celegans --verbose
bowtie2-build Caenorhabditis_elegans.WBcel235.dna.toplevel.fa Celegans --verbose
```
## 3 - align
```shell
bowtie2 -x WBcel235/WBcel235 -U SRR20334685.fastq -S SRR20334685.sam
```
# examine how good the alignment is
```shell
awk '{if ($4 != 0) print $0}' SRR20334685.sam | wc -l
```
```shell
bowtie2 -x WBcel235/WBcel235 -U SRR20334685.fastq -S SRR20334685.sam --verbose
```
```shell
awk '{if ($4 != 0) print $0}' SRR20334685.sam | wc -l
```
```shell
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10 --trim3 20
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10 --trim3 25
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10 --trim3 20 --trim5 5
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10 --trim3 25 --trim5 5
bowtie2 -x Celegans -U SRR20334685.fastq -S SRR20334685.sam --verbose --threads 10 --trim3 25 
```
```shell
awk '{if ($4 != 0) print $0}' SRR20334685.sam | wc -l
```
```shell
awk '{if ($4 != 0) print $0}' SRR20334685.sam | less
```
```shell
bowtie2 -x WBcel235/WBcel235 -U SRR20334685.fastq -S SRR20334685.bw-index.sam --verbose --threads 10 --trim3 25 
```

# D. ALIGNMENT QC - see http://www.htslib.org/workflow/fastq.html
## 1 - samtools 
Visit http://www.htslib.org/download/.
## 2 - htslib 
Visit http://www.htslib.org/download/.
## 3 - fix mate pair errors
```shell
samtools fixmate -O bam,level=1 SRR20334685.sam SRR20334685.fixmate.bam --threads 10 --verbosity 3
samtools view SRR20334685.sam | less
```
## 4 - mark duplicates (prep)
```shell
samtools fixmate -O bam,level=1 -m SRR20334685.sam SRR20334685.fixmate.bam
```
## 5 - sorting
```shell
samtools sort -l 1 -@8 -o SRR20334685.sort.bam -T /tmp/ SRR20334685.fixmate.bam 
samtools view SRR20334685.fixmate.bam | less
samtools view SRR20334685.sort.bam | less
```
## 6 - mark duplicates (marking)
```shell
samtools markdup -O bam,level=1 SRR20334685.sort.bam SRR20334685.markdup.bam 
samtools view SRR20334685.markdup.bam | less
```
## 7 - finalise as BAM or CRAM
```shell
samtools view -@8 SRR20334685.markdup.bam -o SRR20334685.final.bam
samtools view -T Caenorhabditis_elegans.WBcel235.dna.toplevel.fa -@8 SRR20334685.markdup.bam -o SRR20334685.final.cram
samtools view SRR20334685.final.bam | less
samtools view SRR20334685.final.bam | wc -l
samtools view SRR20334685.markdup.bam | wc -l
samtools view SRR20334685.fixmate.bam | wc -l
samtools view SRR20334685.sam | wc -l
samtools view SRR20334685.final.cram | less
samtools index SRR20334685.final.bam --verbosity 3
```

# E. QUANTIFICATION
## 1 - get genome annotation
```shell
wget http://ftp.ensembl.org/pub/release-107/gtf/caenorhabditis_elegans/Caenorhabditis_elegans.WBcel235.107.gtf.gz
```
## 2 - simple quantification using HTSeq
```shell
htseq-count SRR20334685.final.bam Caenorhabditis_elegans.WBcel235.107.gtf -o SRR20334685.count.bam -p bam -n 10
htseq-count SRR20334685.final.bam Caenorhabditis_elegans.WBcel235.107.gtf -o SRR20334685.count.bam -p bam -n 10 --stranded=no -a 0 -t gene
```


# E. VARIANT CALLING (!!!!!won't cover!!!!!)
## 1 - index BAM
```shell
samtools index -@ 10 SRR20334685.final.bam 
```
## 2 - bcftools 
Visit http://www.htslib.org/download/ to download the source code.
## 3 - mpileup and call variants
```shell
bcftools mpileup -Ou -f Caenorhabditis_elegans.WBcel235.dna.toplevel.fa SRR20334685.final.bam | bcftools call -vmO z -o SRR20334685.vcf.gz
```
## 4 - index vcf
```shell
tabix -p vcf SRR20334685.vcf.gz
``` 
