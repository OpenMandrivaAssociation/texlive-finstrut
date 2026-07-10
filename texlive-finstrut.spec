%global tl_name finstrut
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Adjust behaviour of the ends of footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/finstrut
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/finstrut.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX internal command \@finalstrut is used automatically used at
the end of footnote texts to insert a strut to avoid mis-spacing of
multiple footnotes. Unfortunately the command can cause a blank line at
the end of a footnote. The package provides a solution to this problem.

