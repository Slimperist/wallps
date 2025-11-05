#!/usr/bin/env bash
# run_wpscrab.sh
# Обёртка для безопасного запуска z_wpscrab.py
# Положи в /var/www/u3314206/data/www/wallps.fun/run_wpscrab.sh
# Сделай chmod +x run_wpscrab.sh
# Запуск: /var/www/u3314206/data/www/wallps.fun/run_wpscrab.sh

set -uo pipefail

# Параметры — при необходимости поправь
PROJECT_DIR="/var/www/u3314206/data/www/wallps.fun"
VENV_PYTHON="/var/www/u3314206/data/djangoenv/bin/python"
LOCKFILE="/tmp/wpscrab.lock"
LOGFILE="$PROJECT_DIR/logs/cron_wpscrab.log"
SCRIPT="z_wpscrab.py"

# Гарантируем существование лога
mkdir -p "$(dirname "$LOGFILE")"
touch "$LOGFILE"
chmod 664 "$LOGFILE" 2>/dev/null || true

cd "$PROJECT_DIR" || { echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: project dir not found: $PROJECT_DIR" >> "$LOGFILE"; exit 1; }

# Берём lock, если не удалось — выходим (чтобы не дублировать)
(
  flock -n 9 || { echo "$(date '+%Y-%m-%d %H:%M:%S') - INFO: previous job still running, exiting" >> "$LOGFILE"; exit 0; }

  echo "=== START $(date '+%Y-%m-%d %H:%M:%S') ===" >> "$LOGFILE"

  # (опционально) экспорт настроек Django, если в скрипте нет django.setup()
  # export DJANGO_SETTINGS_MODULE="wallpsite.settings"

  # Запуск через python из виртуального окружения
  if [ -x "$VENV_PYTHON" ]; then
      "$VENV_PYTHON" "$PROJECT_DIR/$SCRIPT" >> "$LOGFILE" 2>&1
      RC=$?
  else
      # fallback: если не найден python в виртуальном env - пробуем system python (нежелательно)
      python "$PROJECT_DIR/$SCRIPT" >> "$LOGFILE" 2>&1
      RC=$?
  fi

  echo "=== END $(date '+%Y-%m-%d %H:%M:%S') (rc=$RC) ===" >> "$LOGFILE"
  # при ошибке - можно добавить уведомление тут (email / webhook)
) 9>"$LOCKFILE"