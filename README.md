# CovCal
# author: kk361

Usage: 


	./Cov -i input.fasta -u unpaired.fastq -1 1.fq -2 2.fq -t Thread[default = 1]
	
CovCal is written in Python and is executed from the command line. To install CovCal simply download the latest release of the code from the [Releases page](https://github.com/kk361hit/CovCal.git) and extract the files into a Bismark installation folder.
	
CovCal needs the following tools to be installed and ideally available in the `PATH` environment:
* [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/) 
* [Samtools](http://www.htslib.org/)
