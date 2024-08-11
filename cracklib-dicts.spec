Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de.UTF-8):	Standard-Wörterbücher (/usr/share/dict/words)
Summary(es.UTF-8):	Diccionarios para chequeo de contraseñas
Summary(fr.UTF-8):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl.UTF-8):	Standardowe słowniki (/usr/share/dict/words)
Summary(pt_BR.UTF-8):	Dicionários para checagem de senhas
Summary(ru.UTF-8):	Стандартные словари CrackLib
Summary(tr.UTF-8):	Standart sözlükler (/usr/share/dict/words)
Summary(uk.UTF-8):	Стандартні словники CrackLib
Name:		cracklib-dicts
Version:	2.10.2
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/cracklib/cracklib/releases
Source0:	https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-words-%{version}.bz2
# Source0-md5:	94e9963e4786294f7fb0f2efd7618551
URL:		https://github.com/cracklib/cracklib
BuildRequires:	cracklib-devel >= 2.10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words.

%description -l de.UTF-8
Enthält die Cracklib-Wörterbücher für die
Standard-/usr/share/dict/Wörter sowie Utilities zum Erstellen neuer
Wörterbücher"

%description -l es.UTF-8
Incluye el diccionario cracklib para el padrón /usr/share/dict/words,
y utilitarios necesarios a creación de nuevos diccionarios.

%description -l fr.UTF-8
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires nécessaires à la création de
nouveaux dictionnaires.

%description -l pl.UTF-8
Pakiet zawiera słowniki crackliba, instalowane zwykle jako
/usr/share/dict/words.

%description -l pt_BR.UTF-8
Inclui o dicionário cracklib para o padrão /usr/dict/words, bem como
utilitários necessários a criação de novos dicionários.

%description -l ru.UTF-8
Пакет cracklib-dicts включает словари CrackLib. CrackLib будут нужны
словари, соответствующие вашей системе, которые обычно находятся в
/usr/share/dict/words.

%description -l tr.UTF-8
/usr/share/dict/words dosyası için 'cracklib' kitaplıklarını ve yeni
sözlükler yaratılması için gerekli yardımcı programları içerir.

%description -l uk.UTF-8
Пакет cracklib-dicts містить словники CrackLib. CrackLib будуть
потрібні словники, що відповідають вашій системі, котрі зазвичай
знаходяться в /usr/share/dict/words.

%prep
%setup -qcT
install -d dicts
ln -s %{SOURCE0} dicts

%build
export PATH=/usr/sbin:$PATH

bzip2 -dc dicts/*.bz2 | cracklib-format - | cracklib-packer cracklib_dict

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dict
cp -a cracklib_dict* $RPM_BUILD_ROOT%{_datadir}/dict

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/dict/cracklib_dict.*
