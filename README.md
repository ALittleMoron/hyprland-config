# Hyprland Config

## Описание

Данный репозиторий хранит скрипт для установки и настройки hyprland + dotenv файл, которые можно использовать отдельно без скрипта.

Скрипт и конфиг работают только на Arch Linux. Можете воспользоваться dotenv файлами с небольшими правками для использования в других дистрибутивах.

## Краткая информация

OS: Arch Linux
WM: Hyprland
Terminal: alacritty
Shell: zsh
Bar: Waybar
Fonts: JetBrainsMono Nerd Font
GTK: Ayu-Mirage-Dark (Custom)
wofi: ayu-mirage (Custom)
Icons: Papirus-Dark

## Nvidea

! данный этап не пригодится, если будет использован скрипт.

Для использования hyprland с видеокартами nvidea нужно установить следующие пакеты:

```
yay -S linux-headers nvidia-dkms qt5-wayland qt5ct libva libva-nvidia-driver-git
```

Далее необходимо добавить пакеты `nvidia nvidia_modeset nvidia_uvm nvidia_drm` в `/etc/mkinitcpio.conf`

Сгенерировать новый "слепок" командой `sudo mkinitcpio --config /etc/mkinitcpio.conf --generate /boot/initramfs-custom.img`

Добавить строку `options nvidia-drm modeset=1` в `/etc/modprobe.d/nvidia.conf`

и перезапустить систему (reboot).

## Основные пакеты

! данный этап не пригодится, если будет использован скрипт.

Команда для установки основных пакетов, использущихся в конфиге:

```
yay -S hyprland alacritty jq mako waybar-hyprland swww swaylock-effects \
       wofi wlogout xdg-desktop-portal-hyprland swappy grim slurp thunar \
       polkit-gnome python-requests pamixer pavucontrol brightnessctl bluez \
       bluez-utils blueman network-manager-applet gvfs thunar-archive-plugin \
       file-roller btop pacman-contrib zsh ttf-jetbrains-mono-nerd \
       noto-fonts-emoji lxappearance xfce4-settings sddm-git sddm-theme-astronaut \
       wl-color-picker gsimplecal aritim-dark-gtk-git papirus-icon-theme apple-fonts \
       thunderbird gnome-clock
```

Помимо основных пакетов есть ещё всякое дополнительное, чем я пользуюсь, но добавлять сюда и в скрипт установки
я это не буду для того, чтобы не увеличивать время установки ещё больше. Некоторые пакеты ставятся очень
долго.

## Вспомогательные пакеты

Вспомогательные пакеты нужны Просто для работы со всякими сторорнними приложениями, либо это
утилиты, которые я использую в терминате.

Команда для уставки вспомогательных пакетов следующая:

```
yay -S ripgrep fzf bat exa git-delta gwenview buttercup vivaldi pyenv gdu bottom lazygit nodejs \
       npm
```

Список не полный. В основном, я устанавливаю всё по ситуации + тут не указаны большие программы.
Их можно установить на свой вкус.

## TODO

- [x] alt + tab / Win + tab для переходов по открытым приложениям либо рабочим столам.
- [x] доработать стили под использование темы ayu.
- [x] оставить единственный конфиг без разделения на версии (оставить четвертую).
- [ ] забиндить нотификацию о изменении громкости на кнопки наушников.
- [x] поменять API погоды, либо поправить нынешнее, чтобы использовать координаты, либо конкретные города (сейчас абстрактно всегда Ставрополь).
- [x] добавить календарь (если получится, интерактивный).
- [x] добавить смену раскладки по нажатию на иконку в трее.
- [x] добавить более подробную информацию по наведению на дату и время.
- [x] добавить запуск календаря при нажатии на дату и время.
- [x] заменить все использования команд в конфиге на исполнение скриптов (перенисти в папку scripts).
- [ ] изменить скрипт установки под себя.
- [x] поменять иконки уведомлений на более подходящие для ayu-темы.
- [x] поменять фон для экрана входа в систему.

доработка тачпада:

[x] переключение между рабочими столами смахиванием тремя пальцами влево и вправо.

## Баги

- [x] update_sys.sh не работает. Просто пропадает кнопка, и всё.
- [x] cpu виджет отображает информацию некорректно + не работает нажатие на него.
- [x] иногда не отображается виджет погоды.
- [x] вообще не отображается виджет температуры комплектующих.
- [ ] source и volume у микрофона отображается некорректно.

## Примечания

Данный репозиторий был позаимствован [отсюда](https://github.com/SolDoesTech/HyprV4), но
из-за того, что я достаточно сильно его изменил, то не делал форк. Ставлю звездочку и передаю
огромные слова благодарности автору оригинала.

Также некоторые части кода были взяты [отсюда](https://github.com/JaKooLit/Hyprland-v3), но
на данном конфиге я не строил свой конфиг полностью. Позаимствовал лишь структуру конфига и
небольшие участки кода. Такая же огромная хвала автору!

Сам скрипт ещё не тестировал. Был взят из первой ссылки и доработан согласно моим изменениям, но
тесты не проводились. Уберу данную строку, когда самолично проверю работу конфига.

Также, для нормальной работы hyprland нужно поправить конфиги в следующих местах:

1. В waybar установить клавиатуру в модуле `hyprland/language` для правильного отображения текущей раскладки.
2. Установить раскладку в hyprland.conf, если нужна дополнительная.
3. Установить обои для рабочего стола.
