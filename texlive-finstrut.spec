Name:		texlive-finstrut
Version:	21719
Release:	1
Summary:	Adjust behaviour of the ends of footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/finstrut
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX internal command \@finalstrut is used automatically
used at the end of footnote texts to insert a strut to avoid
mis-spacing of multiple footnotes. Unfortunately the command
can cause a blank line at the end of a footnote. The package
provides a solution to this problem.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/finstrut/finstrut.sty
%doc %{_texmfdistdir}/doc/latex/finstrut/README
%doc %{_texmfdistdir}/doc/latex/finstrut/SRCFILEs.txt
%doc %{_texmfdistdir}/doc/latex/finstrut/finstrut.pdf
%doc %{_texmfdistdir}/doc/latex/finstrut/fstrutst.pdf
#- source
%doc %{_texmfdistdir}/source/latex/finstrut/finstrut.tex
%doc %{_texmfdistdir}/source/latex/finstrut/fstrutst.tex
%doc %{_texmfdistdir}/source/latex/finstrut/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
