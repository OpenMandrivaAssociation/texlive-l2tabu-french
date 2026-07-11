%global tl_name l2tabu-french
%global tl_revision 31315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	French translation of l2tabu
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/l2tabu/french
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-french.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
French translation of l2tabu.

