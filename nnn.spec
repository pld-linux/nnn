# TODO:
# - package rest of scripts/
#
Summary:	The missing terminal file browser for X
Name:		nnn
Version:	2.1
Release:	1
License:	BSD
Group:		Applications/Console
Source0:	https://github.com/jarun/nnn/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6c4094064a9e8edbc73c0f37c6d4ccf0
Patch0:		%{name}-no-rebuild-on-install.patch
URL:		https://github.com/jarun/nnn
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nnn is probably the fastest and most resource-sensitive (with all its
capabilities) file browser you have ever used. It's extremely flexible
too - integrates with your DE and favourite GUI utilities, works with
the desktop opener, supports bookmarks, has smart navigation
shortcuts, navigate-as-you-type mode, disk usage analyzer mode,
comprehensive file details and much more. nnn was initially forked
from noice but is significantly different today.

Cool things you can do with nnn:

 - open any file in the default desktop application or a custom one
 - navigate-as-you-type (search-as-you-type enabled even on directory
   switch)
 - check disk usage with number of files in current directory tree
 - run desktop search utility (gnome-search-tool or catfish) in any
   directory
 - copy absolute file paths to clipboard, spawn a terminal and use the
   paths
 - navigate instantly using shortcuts like ~, -, & or handy bookmarks
 - use cd ..... at chdir prompt to go to a parent directory
 - detailed file stats, media info, list and extract archives
 - pin a directory you may need to revisit and jump to it anytime
 - lock the current terminal after a specified idle time
 - change directory on exit

%package -n bash-completion-nnn
Summary:	bash-completion for nnn
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla nnn
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-nnn
This package provides bash-completion for nnn.

%description -n bash-completion-nnn -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla nnn.

%package -n fish-completion-nnn
Summary:	Fish completion for nnn command
Summary(pl.UTF-8):	Dopełnianie parametrów w fish dla polecenia nnn
Group:		Applications/Shells
Requires:	fish
Requires:	nnn = %{version}-%{release}

%description -n fish-completion-nnn
Fish completion for nnn command.

%description -n fish-completion-nnn -l pl.UTF-8
Dopełnianie parametrów w fish dla polecenia nnn.

%package -n zsh-completion-nnn
Summary:	Zsh completion for nnn command
Summary(pl.UTF-8):	Dopełnianie parametrów w zsh dla polecenia nnn
Group:		Applications/Shells
Requires:	nnn = %{version}-%{release}
Requires:	zsh

%description -n zsh-completion-nnn
Zsh completion for nnn command.

%description -n zsh-completion-nnn -l pl.UTF-8
Dopełnianie parametrów w zsh dla polecenia nnn.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install -Dpm0644 -t $RPM_BUILD_ROOT%{bash_compdir} \
  scripts/auto-completion/bash/nnn-completion.bash
install -Dpm0644 -t $RPM_BUILD_ROOT%{fish_compdir} \
  scripts/auto-completion/fish/nnn.fish
install -Dpm0644 -t $RPM_BUILD_ROOT%{zsh_compdir} \
  scripts/auto-completion/zsh/_nnn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n bash-completion-nnn
%defattr(644,root,root,755)
%{bash_compdir}/nnn-completion.bash

%files -n fish-completion-%{name}
%defattr(644,root,root,755)
%{fish_compdir}/nnn.fish

%files -n zsh-completion-%{name}
%defattr(644,root,root,755)
%{zsh_compdir}/_nnn
