%global tl_name mucproc
%global tl_revision 43445

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Conference proceedings for the German MuC-conference
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mucproc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mucproc.cls is a document class to support the formatting guidelines
for submissions to the German Mensch und Computer conference. This work
consists of the files mucproc.dtx and mucproc.ins and the derived files
mucproc.cls, mucfontsize10pt.clo. A compilable demonstration file using
the mucproc class can be found on https://github.com/Blubu/mucproc/.
This example fulfills the formatting guidelines for MuC 2017.

