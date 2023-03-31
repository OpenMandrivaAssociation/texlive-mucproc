Name:		texlive-mucproc
Version:	43445
Release:	2
Summary:	Conference proceedings for the German MuC-conference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mucproc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mucproc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mucproc.cls is a document class to support the formatting
guidelines for submissions to the German Mensch und Computer
conference. This work consists of the files mucproc.dtx and
mucproc.ins and the derived files mucproc.cls,
mucfontsize10pt.clo. A compilable demonstration file using the
mucproc class can be found on
https://github.com/Blubu/mucproc/. This example fulfills the
formatting guidelines for MuC 2017.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mucproc
%{_texmfdistdir}/tex/latex/mucproc
%doc %{_texmfdistdir}/doc/latex/mucproc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
