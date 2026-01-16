# Tutorial for BASALT

## ⏬ BASALT v1.2.0 INSTALLATION
1. BASALT 1.2.0 installation

   Please refer to the installation guide of BASALT v1.2.0:
   ```
   git clone https://github.com/EMBL-PKU/BASALT.git

   cd BASALT

   conda create -n basalt_env -c conda-forge -c bioconda \     python=3.12 \     megahit metabat2 maxbin2 concoct prodigal semibin \     bedtools blast bowtie2 diamond checkm2 \     unicycler spades samtools racon pplacer pilon \     ncbi-vdb minimap2 miniasm idba hmmer entrez-direct \     biopython uv --yes

   conda activate basalt_env

   uv pip install tensorflow torch torchvision tensorboard tensorboardx \     lightgbm scikit-learn numpy==1.26.4 python-igr
   aph scipy pandas matplotlib \     cython biolib joblib tqdm requests checkm-genome
   ```

   Download BASALT Deep Learning Model Weights:

   ```
   # please chanage the download path according to your computer environment
    
   python BASALT_models_download.py --path "my_model_folder"
   ```
   
   Download BASALT script files and change permission:

   ```
   chmod +x install.sh

   bash install.sh

   chmod +x /path/to/basalt/bin/*
   ```

   Set environment variables by adding the following lines to your ~/.bashrc file:
   ```
   nano ~/.bashrc

   export CHECKM2DB=/path/to/checkm2db/CheckM2_database/uniref100.KO.1.dmnd
   export CHECKM_DATA_PATH=/path/to/checkmdb
   export BASALT_WEIGHT=/path/to/BASALT

   source ~/.bashrc
   ```
   The below Google Drive link provide the essential files for checkm_db, checkm2_db and newest **singularity image**.
   
   ```
   https://drive.google.com/drive/folders/1d0e_2FpYRBAZLwKXl8fA-yDK4b5PBA_E?usp=sharing
   ```

   ⚠️: **Another way** to install BASALT in China mainland 以singularity的方式加载BASALT的sif镜像
      
   将BASALT的singularity镜像（basalt.sif）放置在服务器的home目录下。以执行singularity的命令运行，如
   ```
   singularity run basalt.sif BASALT -a as1.fa -s S1_R1.fq,S1_R2.fq/S2_R1.fq,S2_R2.fq -t 32 -m 128
   ```

   如basalt.sif不在home目录下运行需要添加 -B挂载，如
   ```
   # please change /meida/emma according to your path
   singularity run -B /media/emma basalt.sif BASALT -h
   ```

   需要后台挂载运行，nohup可能会出现意外，但是集群一般sbatch等提交命令的方式可以正常运行。实验室的服务器则考虑使用screen命令。
请严格参考screen命令的执行方式（除非你很熟悉screen，切勿擅自修改命令执行方式）。如
   ```
    screen -dmS session_name bash -c 'bash basalt.sh >log_basalt'
   ```
   请注意session_name要起跟自己有辨识度唯一的名字，避免发生意外情况

   basalt.sif含有checkm1 checkm2 semibin  bowtie2 bwa等很多软件，均可以通过以下方式调用：
   ```
   singularity run basalt.sif bowtie2 -h
   ```

## ⏬ BASALT v1.1.0 INSTALLATION

1.	Quick installation 
   
   Download BASALT_setup.py and run:
   ```
   python BASALT_setup.py
   ```
   Please remain patient, as the installation process may take an extended period.

2. Quick installation from China mainland 从中国内地快速安装BASALT
   
   For users in China mainland who may experience a network issue, please download the alternative script ‘BASALT_setup_China_mainland.py’ and run:

   中国内地且无法翻墙的用户推荐使用‘BASALT_setup_China_mainland.py’安装
   ```
   python BASALT_setup_China_mainland.py
   ```
   Then, download the trained models for neural networks BASALT.zip from Tencent iCloud (https://share.weiyun.com/r33c2gqa) and run:
   ```
   mv BASALT.zip ~/.cache
   cd ~/.cache
   unzip BASALT.zip
   ```

3. Manual installation (recommended)
   
   Install Miniconda (https://docs.anaconda.com/free/miniconda/miniconda-install/) or Anaconda (https://docs.anaconda.com/free/anaconda/install/index.html)

   Add mirrors to increase download speed of BASALT dependent software (optional):
   ```
   site=https://mirrors.tuna.tsinghua.edu.cn/anaconda
   conda config --add channels ${site}/pkgs/free/
   conda config --add channels ${site}/pkgs/main/
   conda config --add channels ${site}/cloud/conda-forge/
   conda config --add channels ${site}/cloud/bioconda/
   ```

   Download the BASALT installation file and create a conda environment:
   ```
   git clone https://github.com/EMBL-PKU/BASALT.git
   cd BASALT
   conda env create -n BASALT --file basalt_env.yml
   ```

   Please remain patient, as the installation process may take an extended period.

   If you have encountered an error, please download 'basalt_env.yml' from Tencent iCloud (https://share.weiyun.com/xXdRiDkl) and create a conda environment:
   ```
   conda env create -n BASALT --file basalt_env.yml
   ```

   After successfully creating the conda environment, change file permissions for BASALT script files:
   ```  
   chmod -R 777 <PATH_TO_CONDA>/envs/BASALT/bin/*
   ```
   Example: To easily find your path to conda environments, simply use:
   ```
   conda info --envs
   ```
   and you can find your path to BASALT environment, such as:
   ```
   # conda environments:
   #
   base     /home/emma/miniconda3
   BASALT   /home/emma/miniconda3/envs/BASALT
   ```
   Then, change permission to BASALT script folders:
   ```
   chmod -R 777 /home/emma/miniconda/envs/BASALT/bin/*
   ```

   Download the trained models for neural networks 'BASALT.zip' from FigShare:

   > You can also find the BASALT v1.1.0 version BASALT.zip file the previous released version and download it
   
   ```
   wget https://figshare.com/ndownloader/files/41093033
   mv 41093033 BASALT.zip
   mv BASALT.zip ~/.cache
   cd ~/.cache
   unzip BASALT.zip
   ```
   For users from China mainland, please download the models BASALT.zip from Tencent iCloud (https://share.weiyun.com/r33c2gqa) and run:
   ```
   mv BASALT.zip ~/.cache
   cd ~/.cache
   unzip BASALT.zip
   ```

5. Another way to install BASALT in China mainland 以singularity的方式加载BASALT的sif镜像

   使用BASALT,可通过微云的以下网址获得BASALT.sif镜像文件
   ```
   https://share.weiyun.com/xKmoBmrF
   ```
      
   将BASALT的singularity镜像（BASALT.sif）放置在服务器的home目录下。以执行singularity的命令运行，如
   ```
   singularity run BASALT.sif BASALT -a as1.fa -s S1_R1.fq,S1_R2.fq/S2_R1.fq,S2_R2.fq -t 32 -m 128
   ```

   如BASALT.sif不在home目录下运行需要添加 -B挂载，如
   ```
   singularity run -B /media/emma BASALT.sif BASALT -h
   ```

   需要后台挂载运行，nohup可能会出现意外，但是集群一般sbatch等提交命令的方式可以正常运行。实验室的服务器则考虑使用screen命令。
请严格参考screen命令的执行方式（除非你很熟悉screen，切勿擅自修改命令执行方式）。如
   ```
    screen -dmS session_name bash -c 'bash basalt.sh >log_basalt'
   ```
   请注意session_name要起跟自己有辨识度唯一的名字，避免发生意外情况

   BASALT.sif含有checkm1 checkm2 semibin  bowtie2 bwa等很多软件，均可以通过以下方式调用：
   ```
   singularity run BASALT.sif bowtie2 -h
   ```
   
6. Test files
   Sample demo files (see BASALT demo files) are prepared for testing whether the BASALT script can be successfully performed, and the bins can be generated. The demo files contain Data.tar.gz, Final_bestbinset.tar.gz and basalt.sh.
   ```
   Data.tar.gz -> short read and long read raw sequence files and an OPERA-MS assembled contig file.
   Final_bestbinset.tar.gz -> expected output of final bins.
   basalt.sh -> script running this demo
   ```
   A workstation with a configuration of Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz with 32 cores is expected to complete processing of this demo dataset within 6 hours.



## 🧪 USAGE
1.	General usage

  	To run BASALT, use BASALT under conda environment, or use BASALT.py for standalone users:
   ```
   BASALT [-h] [-a ASSEMBLIES] [-s SR_DATASETS] [-l LONG_DATASETS] [-hf HIFI_DATASET] [-c HI_C_DATASET] [-t THREADS] [-m RAM] [-e EXTRA_BINNER] [-qc QC_SOFTWARE] [--min-cpn MIN_COMPLETENESS] [--max-ctn MAX_CONTAMINATION] [--mode RUNNING_MODE] [--module FUNCTIONAL_MODULE] [--autopara AUTOBINING_PARAMETERS] [--refinepara REFINEMENT_PARAMTER]![image](https://github.com/EMBL-PKU/BASALT/assets/62051720/61fb5b05-2844-4867-9598-f91e0709fa9a)
   ```
   Required arguments
   
   ```
   -a	list of assemblies, e.g., -a assembly1.fa,assembly2.fa
   Files ending with .fa, .fna, and .fasta are all supported. Additionally, compressed files ending with .gz, .tar.gz, and .zip are also supported.
   
   -s	short-read datasets, e.g., -s d1_r1.fq,d1_r2.fq/d2_r1.fq,d2_r2.fq
   Please note, read files within each pair are separated with ‘,’, and read pairs are separated with ‘/’. Reads files ending with .gz, .tar.gz, and .zip are also supported.
   
   -l		long-read datasets, e.g., -l lr1.fq,lr2.fq
   
   -hf	PacBio-HiFi datasets, e.g., -hf hifi1.fq,hifi2.fq
   
   -c	Hi-C datasets, e.g., -c hc1.fq,hc2.fq
   Read files within each pair are separated with ‘,’. Reads files ending with .gz, .tar.gz, and .zip are also supported.
   
   -t	number of threads, e.g., -t 32
   
   -m	RAM, e.g., -m 128
   Suggested minimum RAM is 32G.
   ```
   Optional arguments
   ```
   --min-cpn		Minimum completeness cutoff, e.g., --min-cpn 30 (default: 35)
   
   --max-ctn		Maximum contamination cutoff, e.g., --max-ctn 25 (default: 20)
   
   --mode		Running mode. Start a new project from the beginning –-mode new or continue the previous run –-mode continue. (default: continue)
   
   --module		Running mode. Run only Autobinning + Bin Selection modules –-module autobinning, Refinement module –-module refinement, Gap filling module –-module reassembly, or running all modules –-module all. (default: all)
   
   --autopara		Autobinning parameters. 
   –-autopara more-sensitive Choose recommended binners with full parameters: Maxbin2 [0.3, 0.5, 0.7, 0.9], MetaBAT2 [200, 300, 400, 500], CONCOCT [2-3 flexible parameters based on result of MetaBAT2], and Semibin2 [100]
   –-autopara sensitive Partial binners with partial parameters: MetaBAT2 [200, 300, 400, 500], CONCOCT [1-2 flexible parameters based on result of MetaBAT2], and Semibin2 [100]
   –-autopara quick Limited binners: MetaBAT2 [200, 300, 400, 500] and Semibin2 [100]
(default: more-sensitive)

   --refinepara	Refinement parameters. 
   --refinepara deep will enable deep refinement at sequence retrieval step. Disable this function by setting the parameter with 
   –-refinepara quick. (default: deep)
   
   --hybrid_reassembly	Setting hybrid reassembly parameters. In reassembly function, BASALT uses SPAdes Hybrid function as default parameter
   –-hybrid_assembly n to process hybrid reassembly in the existence of SRS and LRS. Use –-hybrid_assembly y to use Unicycler for hybrid reassembly. Please note that it will take a considerable amount of time when using Unicycler for hybrid reassembly.

   -q			Selection of quality check software. Default: checkm. If you want to use CheckM2, by setting with –q checkm2.
   
   -e			Enable extra binners. We temporarily disabled VAMB in BASALT v1.0.1. To enable Metabinner, use –e m in addition to other binners
   
   -h 			Help documents.
   ```

2.	Example
   Run BASALT based on SRS datasets:
   ```
   BASALT\
   -a as1.fa,as2.fa,as3.fa\
   -s srs1_r1.fq,srs1_r2.fq/srs2_r1.fq,srs2_r2.fq\
   -t 60 -m 250
   ```

   Run BASALT based on SRS + LRS datasets:
   ```
   BASALT\
   -a as1.fa,as2.fa,as3.fa\
   -s srs1_r1.fq,srs1_r2.fq/srs2_r1.fq,srs2_r2.fq\
   -l lrs1.fq,lrs2.fq -t 60 -m 250
   ```

   Run BASALT based on customized parameters:
   ```
   BASALT\
   -a as1.fa,as2.fa,as3.fa\
   -s srs1_r1.fq,srs1_r2.fq/srs2_r1.fq,srs2_r2.fq\
   -l lr1.fq,lr2.fq -hf hifi1.fq\
   -t 60 -m 250\
   --autopara sensitive --refinepara quick --min-cpn 40 --max-ctn 15 -qc checkm2
   ```



## 🙋 Troubleshooting
1.	Error from SAMtools when installing BASALT:
   ```
   samtools: error while loading shared libraries: libcrypto.so1.0.0: cannot open shared object file: No such file or directory
   ```
   Troubleshooting: Check the file libcrypto.so1.0.0:
   ```
   ls <PATH_TO_CONDA>/envs/BASALT/lib/libcry*
   ```
   If libcrypto.so.1.1 was found instead of libcrypto.so.1.0.0, create a soft link of libcrypto.so.1.1 to libcrypto.so.1.0.0:
   ```
   cd <PATH_TO_CONDA>/envs/BASALT/lib
   ln -s libcrypto.so.1.1 libcrypto.so.1.0.0
   ```
   Then check if SAMtools is available:
   ```
   samtools -help
   ```
2.	Error encountered when running BASALT:
   ```
   Traceback (most recent call last):
   File "/users/.conda/envs/BASALT/bin/BASALT", line 57, in
   datasets[str(n)].append(pr[1].strip())
   IndexError: list index out of range
   ```
   This is because BASALT does not support reading files with absolute path. To address this issue, simply move/copy corresponding files to the working directory or establish soft links under the working directory.
   
3.	Error encountered when running BASALT:
   ```
   Traceback (most recent call last):
   File "/users/.conda/envs/BASALT/bin/BASALT", line 53, in 
   datasets_list=sr_datasets.split('/')
   ```
   This is because BASALT does not support LRS only mode except PacBio-HiFi reads in v1.0.1. Please use SRS + LRS instead of LRS only. LRS only mode for Nanopore/PacBio long reads will be available in v1.0.2.

4.	Error encountered when running BASALT:
   ```
   INFO: Running CheckM2 version 1.0.1
   [03/13/2024 12:56:34 PM] INFO: Running quality prediction workflow with 30 threads.
   [03/13/2024 12:56:34 PM] ERROR: DIAMOND database not found. Please download database using <checkm2 database --download>
   ```
   This is because CheckM2 database is not installed. Users can simply download CheckM2 database from their official website (https://github.com/chklovski/CheckM2) to address this issue.

5.	Error encountered when running BASALT:
   ```
   BASALT: command not found!
   ```
   This issue occurred because BASALT scripts cannot be found or administrated. Please firstly check if BASALT has been successfully installed, by checking script files under the bin folder of BASALT environment, e.g.:
   ```
   <PATH_TO_CONDA>/envs/BASALT/bin/
   ```
   If no script file was found, please download BASALT script again and copy to the bin folder of BASALT environment, by using the following commands:
   ```
   unzip BASALT_script.zip
   chmod -R 777 BASALT_script
   mv BASALT_script/* <PATH_TO_CONDA>/envs/BASALT/bin/
   ```
   If BASALT scripts are found in the bin folder of BASALT environment, try to change permissions by using the following commands:
   ```
   chmod -R 777 <PATH_TO_CONDA>/envs/BASALT/bin/*
   ```
6.	Error encountered when running BASALT:
   ```
   Traceback (most recent call last):
  File "/user/miniconda3/envs/BASALT/bin/BASALT", line 137, in <module>
    BASALT_main_d(assembly_list, datasets, num_threads, lr_list, hifi_list, hic_list, eb_list, ram, continue_mode, functional_module, autobining_parameters, refinement_paramter, max_ctn, min_cpn, pwd, QC_software)
  File "/user/miniconda3/envs/BASALT/bin/BASALT_main_d.py", line 494, in BASALT_main_d
    Contig_recruiter_main(best_binset_from_multi_assemblies, outlier_remover_folder, num_threads, continue_mode, min_cpn, max_ctn, assembly_mo_list, connections_list, lr_connection_list, coverage_matrix_list, refinement_paramter, pwd)
  File "/user/miniconda3/envs/BASALT/bin/S6_retrieve_contigs_from_PE_contigs_10302023.py", line 1819, in Contig_recruiter_main
    parse_bin_in_bestbinset(assemblies_list, binset+'_filtrated', outlier_remover_folder, PE_connections_list, lr_connection_list, num_threads, last_step, coverage_matrix_list, refinement_mode)
  File "/user/miniconda3/envs/BASALT/bin/S6_retrieve_contigs_from_PE_contigs_10302023.py", line 1695, in parse_bin_in_bestbinset
    bin_comparison(str(binset), bins_checkm, str(binset)+'_retrieved', refinement_mode, num_threads)
  File "/user/miniconda3/envs/BASALT/bin/S6_retrieve_contigs_from_PE_contigs_10302023.py", line 731, in bin_comparison
    for line in open('quality_report.tsv','r'):
FileNotFoundError: [Errno 2] No such file or directory: 'quality_report.tsv'
   ```
	
 This is possibly due to the insufficient number of bins generated due to the low coverage of datasets at the current step, which CheckM2 cannot generate quality file.
