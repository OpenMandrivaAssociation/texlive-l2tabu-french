Name:		texlive-l2tabu-french
Epoch:		1
Version:	31315
Release:	2
Summary:	French translation of l2tabu
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/l2tabu/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
French translation of l2tabu.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/README
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/l2tabufr.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-french/l2tabufr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
