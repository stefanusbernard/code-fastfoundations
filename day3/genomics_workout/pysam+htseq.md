>>> reference for rna-seq analysis
https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8

pysam

- read BAM files
	>>> import pysam
	>>> samfile = pysam.AlignmentFile("ex1.bam", "rb")
	- iterate over reads matching to a region using fetch()
	>>> iter = samfile.fetch("seq1", 10, 20)
	>>> for x in iter:
	>>>     print(str(x))

	- write to bam
	- filter reads e.g. read.is_paired
- read SAM files
	>>> import pysam
	>>> samfile = pysam.AlignmentFile("ex1.sam", "r")
	- iterate over each basse of a region using pileup()
	>>> iter = samfile.pileup('seq1', 10, 20)
	>>> for x in iter:
	>>>    print(str(x))
- read CRAM files
	>>> import pysam
	>>> samfile = pysam.AlignmentFile("ex1.cram", "rc")
- all samtools commands are function calls e.g. .sort(args)
	>>> pysam.sort("-o", "output.bam", "ex1.bam")
- tabix files
	- random fast access e.g. file.gtf.gz
	>>> import pysam
	>>> tbx = pysam.TabixFile("example.bed.gz")
	>>> for row in tbx.fetch("chr1", 1000, 2000):
    >>> 	print("chromosome is", row[0])


SAM/BAM/CRAM files API -> https://pysam.readthedocs.io/en/latest/api.html#sam-bam-cram-files



HTSeq
- read and iterate over fastq file
	>>> import HTSeq
	>>> fastq_file = HTSeq.FastqReader("yeast_RNASeq_excerpt_sequence.txt", "solexa")
	>>> import itertools
	>>> for read in itertools.islice(fastq_file, 10):
	...    print(read)

- read and iterate over SAM file
	>>> alignment_file = HTSeq.SAM_Reader("yeast_RNASeq_excerpt.sam")
	>>> nreads = 0
	>>> for aln in alignment_file:
	...    qualsum += aln.read.qual
	...    nreads += 1
	>>> aln.read
	<SequenceWithQualities object 'HWI-EAS225:1:11:76:63#0/1'>
	>>> aln.read.name
	'HWI-EAS225:1:11:76:63#0/1'
	>>> aln.read.seq
	b'ACTGTAAATACTTTTCAGAAGAGATTTGTAGAATCC'
	>>> aln.read.qualstr
	b'BBBB@B?AB?>BAAA@A@>=?=?9=?=;9>988<::'
	>>> aln.read.qual
	array([33, 33, 33, 33, 31, 33, 30, 32, 33, 30, 29, 33, 32, 32, 32, 31, 32,
	       31, 29, 28, 30, 28, 30, 24, 28, 30, 28, 26, 24, 29, 24, 23, 23, 27,
	       25, 25], dtype=uint8)
	>>> aln.iv
	<GenomicInterval object 'IV', [246048,246084), strand '+'>
	>>> aln.iv.chrom
	'IV'
	>>> aln.iv.start
	246048
	>>> aln.iv.end
	246084
	>>> aln.iv.strand
	'+'
	- has an 'aligned' argument

- read and write BAM files
	>>> bam_reader = HTSeq.BAM_Reader("SRR001432_head_sorted.bam")
	>>> for a in itertools.islice(bam_reader, 5):  # printing first 5 reads
	...    print(a)

	>>> bam_writer = HTSeq.BAM_Writer.from_BAM_Reader("region.bam", bam_reader) #set-up BAM_Writer with same header as reader
	>>> for a in bam_reader.fetch(region = "1:249000000-249200000"): #fetching reads in a region
	...    print("Writing Alignment", a, "to file", bam_writer.filename)
	...    bam_writer.write(a)   

- quantification against GTF: https://htseq.readthedocs.io/en/master/htseqcount.html#htseqcount
	>>> gtf_file = HTSeq.GFF_Reader(
	...    "Saccharomyces_cerevisiae.SGD1.01.56.gtf.gz",
	...    end_included=True)
	>>> for feature in itertools.islice(gtf_file, 10):
	...    print(feature)
	>>> feature.iv
	<GenomicInterval object '2-micron', [3270,3813), strand '+'>
	>>> feature.source
	'protein_coding'
	>>> feature.type
	'CDS'
	>>> feature.score
	'.'
	>>> sorted(feature.attr.items())    
	[('exon_number', '1'),
	 ('gene_id', 'R0030W'),
	 ('gene_name', 'RAF1'),
	 ('protein_id', 'R0030W'),
	 ('transcript_id', 'R0030W'),
	 ('transcript_name', 'RAF1')]
	>>> feature.name
	'R0030W'
	>>> exons = HTSeq.GenomicArrayOfSets("auto", stranded=False)
	>>> for feature in gtf_file:
	...    if feature.type == "exon":
	...       exons[feature.iv] += feature.name
	>>> iv = HTSeq.GenomicInterval("III", 23850, 23950, ".")

- manual quantification: https://htseq.readthedocs.io/en/master/counting.html






