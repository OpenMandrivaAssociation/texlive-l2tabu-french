# revision 31315
# category Package
# catalog-ctan /info/l2tabu/french
# catalog-date 2013-07-30 20:12:28 +0200
# catalog-license gpl
# catalog-version 2.3
Name:		texlive-l2tabu-french
Epoch:		1
Version:	2.3
Release:	3
Summary:	French translation of l2tabu
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
