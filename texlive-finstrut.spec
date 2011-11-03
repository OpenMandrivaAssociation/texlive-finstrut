# revision 21719
# category Package
# catalog-ctan /macros/latex/contrib/finstrut
# catalog-date 2011-03-14 20:53:55 +0100
# catalog-license lppl1.3
# catalog-version 0.5
Name:		texlive-finstrut
Version:	0.5
Release:	1
Summary:	Adjust behaviour of the ends of footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/finstrut
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The LaTeX internal command \@finalstrut is used automatically
used at the end of footnote texts to insert a strut to avoid
mis-spacing of multiple footnotes. Unfortunately the command
can cause a blank line at the end of a footnote. The package
provides a solution to this problem.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
