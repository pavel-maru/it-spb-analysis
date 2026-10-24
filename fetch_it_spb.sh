#!/bin/sh

if [ -z "$HH_ACCESS_TOKEN" ]; then
    echo "Error: HH_ACCESS_TOKEN is not set."
    exit 1
fi

# Ищем вакансии по запросу "IT" в регионе 2 (Санкт-Петербург)
# Берем 100 вакансий (максимум за один запрос)
curl -s -G "https://api.hh.ru/vacancies" \
  --data-urlencode "text=IT" \
  --data-urlencode "area=2" \
  --data-urlencode "per_page=100" \
  --data-urlencode "page=0" \
  -H "Authorization: Bearer ${HH_ACCESS_TOKEN}" \
  -H "HH-User-Agent: CustomProject/1.0 (pavel_maru@mail.ru)" \
  -o it_spb_raw.json

# Проверяем на ошибки
if grep -q '"errors"' it_spb_raw.json; then
    echo "API returned an error:"
    cat it_spb_raw.json
    exit 1
fi

echo "Successfully fetched data to it_spb_raw.json"
