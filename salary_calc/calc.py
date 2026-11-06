def calculate_annual_income(title, monthly_salary, months_worked, recovery_cost_per_month=0, severance_months=0):
    """
    Считает годовой доход с учетом расходов на восстановление и выходного пособия.
    """
    # Валовый доход: зарплата за отработанные месяцы + выходное пособие (если есть)
    gross_income = (monthly_salary * months_worked) + (monthly_salary * severance_months)
    
    # Сколько месяцев человек не работал
    unemployed_months = 12 - months_worked
    
    # Расходы на восстановление (для вахтовиков - здоровье, для IT-рисков - жизнь на сбережения)
    recovery_expenses = recovery_cost_per_month * unemployed_months
    
    net_income = gross_income - recovery_expenses
    
    print(f"\n--- {title} ---")
    print(f"Зарплата: {monthly_salary:,} ₽/мес")
    print(f"Работает: {months_worked} мес/год (простой: {unemployed_months} мес)")
    if severance_months > 0:
        print(f"Выходное пособие: {severance_months} окладов")
    print(f"Валовый доход за год: {gross_income:,} ₽")
    print(f"Расходы на восстановление/жизнь в простой: {recovery_expenses:,} ₽")
    print(f"Чистый доход: {net_income:,} ₽")
    print(f"Средний доход в месяц (чистый): {net_income // 12:,} ₽")
    
    return net_income


def main():
    print("=" * 60)
    print("КАЛЬКУЛЯТОР: СТАБИЛЬНАЯ РАБОТА vs ВАХТА vs РИСКИ IT")
    print("=" * 60)

    # Сценарий 1: Стабильный IT (12 месяцев)
    it_stable = calculate_annual_income("1. Стабильный IT-специалист", 100000, 12)

    # Сценарий 2: Вахтовик (6 месяцев вахты, 6 месяцев отдыха, 30к на восстановление)
    vahta = calculate_annual_income("2. Вахтовик (Сахалин/Казахстан)", 400000, 6, recovery_cost_per_month=30000)

    # Сценарий 3: IT-специалист с риском (9 месяцев работы, сокращение, 2 оклада выходного пособия)
    # 3 месяца он ищет работу, тратит накопления (пусть 50к в месяц на жизнь)
    it_risk = calculate_annual_income("3. IT-специалист (сокращение на 3 мес)", 100000, 9, recovery_cost_per_month=50000, severance_months=2)

    print("\n" + "=" * 60)
    print("ВЫВОДЫ:")
    print(f"Стабильный IT: {it_stable:,} ₽")
    print(f"Вахтовик: {vahta:,} ₽")
    print(f"IT с риском: {it_risk:,} ₽")
    
    if it_risk < it_stable:
        diff = it_stable - it_risk
        print(f"Потеря работы на 3 месяца обходится IT-специалисту в {diff:,} ₽ в год!")
    print("=" * 60)


if __name__ == '__main__':
    main()
