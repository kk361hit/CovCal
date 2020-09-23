#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: kk361
 
import sys
import datetime
import getopt
import os


class ProgressBar():

	def __init__(self, max_steps):
		self.max_steps = max_steps
		self.current_step = 0
		self.progress_width = 25
		
	def update(self, step=None):
		self.current_step = step
		num_pass = int(self.current_step * self.progress_width / self.max_steps)
		num_passf = int((self.progress_width - num_pass)*((self.current_step / self.max_steps)*10%1))
		num_rest = self.progress_width - num_pass
		time = str(datetime.datetime.now() - starttime)
		percent = (self.current_step) * 100.0 / self.max_steps 
		progress_bar = "\t" + "█" * (num_pass) + "★" * num_passf +""+ "☆" * (num_rest - num_passf) + " " 
		progress_bar += "%.2f" % percent + "%   time: " +  time
		if self.current_step <= self.max_steps - 1:
			progress_bar += "\r" 
		else:
			progress_bar += "\n" 
		sys.stdout.write(progress_bar) 
		sys.stdout.flush()
		if self.current_step >= self.max_steps:
			self.current_step = 0
			print


def usage():

	print("Usage:")
	print("\tCalcovpy -d depth [-o output_file]")


def main():
	global starttime
	starttime = datetime.datetime.now()
	opts, args = getopt.getopt(sys.argv[1:], "hd:o")
	input_file = ""
	output_file = ""
	prefix=""
	for op, value in opts:
		if op == "-d":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			usage()
			sys.exit()

	if input_file == "":
		usage()
		sys.exit()

	if output_file == "":
		output_file = input_file +".cov.txt"
	
	max_batchs = 0
	for max_batchs, line in enumerate(open(input_file, "rU")):
		max_batchs += 1
	progress_bar = ProgressBar(max_batchs)
	iteration = 0

	depth = open(input_file)
	table_output = open(output_file,"w")
	

	print("Input_file:\t",input_file,"\noutput:\t",output_file,"\nstart at:\t",starttime)
	print("Calulating coverage ...")
	contigs = {}	
	pbcont = 0
	Totaldepth = 0
	for lineD in depth:
		if lineD  != "\n":
			lineD = lineD.strip("\n")
			listD = lineD.split()
			if not (listD[0] in contigs.keys()):
				contigs[listD[0]] = [0,0]
			pbcont += 1
			Totaldepth += int(listD[2])
			contigs[listD[0]][0] = contigs[listD[0]][0] + 1
			contigs[listD[0]][1] += int(listD[2])
		iteration += 1
		progress_bar.update(iteration)
		
	Contigs_sorted = sorted(contigs,key=lambda x: x[0])
	
	for Contig in Contigs_sorted:
		table_output.write(Contig + "\t" + str(contigs[Contig][1]/contigs[Contig][0]) + "\n" )
	
	print("Averge coverage:\t" , str(Totaldepth/pbcont))
	print("Finished!")
	print("Consumed time:\t" , str(datetime.datetime.now() - starttime))

if __name__ == '__main__':
	main()