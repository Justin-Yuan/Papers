# Util bash funcs for paper readings, put them in bashrc file 

# paper reading shortcuts 
export Paper="<Paper repo path>"
## convert paper name to proper format, print and copy to clipboard
pname () {
	case "$(uname -s)" in
		Darwin)
			python -c "import sys; k='_'.join(sys.argv[1:]); print(k)" "$@" | tee >(pbcopy)
			;;
		Linux)
			python -c "import sys; k='_'.join(sys.argv[1:]); print(k)" "$@" | tee >(xclip -selection c)
			;;
		CYGWIN*|MINGW32*|MSYS*|MINGW*)
			echo 'MS Windows'
			;;
		*)
			echo 'Other OS' 
			;;
	esac	
}

## open new markdown file for paper notes 
pnote () {
	CUR_DIR=`pwd`;
	cd $Paper 
	# get formatted name for paper
	pname "$@"
	PAPER_NAME="temp"
	case "$(uname -s)" in
		Darwin)
			PAPER_NAME=`pbpaste`
			;;
		Linux)
			PAPER_NAME=`xclip -selection clipboard -o`
			;;
		CYGWIN*|MINGW32*|MSYS*|MINGW*)
			echo 'MS Windows'
			;;
		*)
			echo 'Other OS' 
			;;
	esac
	# make new note for paper
	PAPER_PATH="$Paper/daily/${PAPER_NAME}.md"
	cp $Paper/templates/template.md $PAPER_PATH
	# open for editing 
	code $PAPER_PATH
	# go back 
	cd $CUR_DIR
}