"""
dashboard window with comprehensive data visualization and modern styling.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates


class DashboardWindow(tk.Toplevel):
    """Enhanced dashboard with comprehensive expense analytics and visualizations."""

    def __init__(self, master, repo):
        super().__init__(master)
        self.title("Expense Analytics Dashboard")
        self.repo = repo
        self.geometry("1200x800")
        self.configure(bg='#f0f0f0')

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self._build_ui()
        self.refresh()

    def _build_ui(self):
        # Main container with notebook for tabs
        main_frame = tk.Frame(self, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Create notebook for organized tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)

        # Tab 1: Overview
        self.overview_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.overview_frame, text="📊 Overview")
        self._build_overview_tab()

        # Tab 2: Charts & Visualizations
        self.charts_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.charts_frame, text="📈 Analytics")
        self._build_charts_tab()

        # Tab 3: Detailed Analysis
        self.analysis_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.analysis_frame, text="🔍 Analysis")
        self._build_analysis_tab()

    def _build_overview_tab(self):
        # Header section
        header_frame = tk.Frame(self.overview_frame, bg='#2c3e50', height=80)
        header_frame.pack(fill='x', padx=5, pady=5)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="💰 Expense Dashboard",
                               font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(pady=20)

        # Summary cards frame
        cards_frame = tk.Frame(self.overview_frame, bg='white')
        cards_frame.pack(fill='x', padx=10, pady=10)

        # Create summary cards
        self._create_summary_cards(cards_frame)

        # Quick insights frame
        insights_frame = tk.LabelFrame(self.overview_frame, text="Quick Insights",
                                       font=('Arial', 12, 'bold'), bg='white')
        insights_frame.pack(fill='x', padx=10, pady=5)

        self.insights_text = tk.Text(insights_frame, height=6, wrap='word',
                                     font=('Arial', 10), bg='#f8f9fa')
        self.insights_text.pack(fill='x', padx=5, pady=5)

        # Recent activity frame - clean Frame with solid border
        recent_container = tk.Frame(self.overview_frame, bg='white')
        recent_container.pack(fill='both', expand=True, padx=10, pady=5)

        tk.Label(recent_container, text="Recent Activity",
                 font=('Arial', 12, 'bold'), bg='white').pack(anchor='w', padx=5, pady=5)

        recent_frame = tk.Frame(recent_container, bd=1, relief='solid', bg='white')
        recent_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create treeview for recent expenses (without Comments column)
        columns = ('Date', 'Category', 'Description', 'Amount')
        self.recent_tree = ttk.Treeview(recent_frame, columns=columns, show='headings', height=8)

        for col in columns:
            self.recent_tree.heading(col, text=col)
            self.recent_tree.column(col, width=150)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient='vertical', command=self.recent_tree.yview)
        self.recent_tree.configure(yscrollcommand=scrollbar.set)

        self.recent_tree.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)

    def _create_summary_cards(self, parent):
        # Total Spent Card
        total_card = tk.Frame(parent, bg='#3498db', relief='raised', bd=2)
        total_card.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        tk.Label(total_card, text="Total Spent", font=('Arial', 12),
                 fg='white', bg='#3498db').pack(pady=5)
        self.total_label = tk.Label(total_card, text="$0.00", font=('Arial', 16, 'bold'),
                                    fg='white', bg='#3498db')
        self.total_label.pack(pady=5)

        # Number of Expenses Card
        count_card = tk.Frame(parent, bg='#e74c3c', relief='raised', bd=2)
        count_card.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        tk.Label(count_card, text="Number of Expenses", font=('Arial', 12),
                 fg='white', bg='#e74c3c').pack(pady=5)
        self.count_label = tk.Label(count_card, text="0", font=('Arial', 16, 'bold'),
                                    fg='white', bg='#e74c3c')
        self.count_label.pack(pady=5)

        # Average Expense Card
        avg_card = tk.Frame(parent, bg='#2ecc71', relief='raised', bd=2)
        avg_card.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        tk.Label(avg_card, text="Average Expense", font=('Arial', 12),
                 fg='white', bg='#2ecc71').pack(pady=5)
        self.avg_label = tk.Label(avg_card, text="$0.00", font=('Arial', 16, 'bold'),
                                  fg='white', bg='#2ecc71')
        self.avg_label.pack(pady=5)

        # Top Category Card
        top_card = tk.Frame(parent, bg='#f39c12', relief='raised', bd=2)
        top_card.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        tk.Label(top_card, text="Top Category", font=('Arial', 12),
                 fg='white', bg='#f39c12').pack(pady=5)
        self.top_category_label = tk.Label(top_card, text="N/A", font=('Arial', 14, 'bold'),
                                           fg='white', bg='#f39c12')
        self.top_category_label.pack(pady=5)

    def _build_charts_tab(self):
        # Create matplotlib figure for charts
        self.fig = Figure(figsize=(12, 8), facecolor='white')

        # Create subplots
        self.ax1 = self.fig.add_subplot(2, 2, 1)
        self.ax2 = self.fig.add_subplot(2, 2, 2)
        self.ax3 = self.fig.add_subplot(2, 2, 3)
        self.ax4 = self.fig.add_subplot(2, 2, 4)

        self.fig.tight_layout(pad=3.0)

        # Embed matplotlib in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.charts_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)

    def _build_analysis_tab(self):
        # Category breakdown frame
        cat_frame = tk.LabelFrame(self.analysis_frame, text="Category Analysis",
                                  font=('Arial', 12, 'bold'), bg='white')
        cat_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Category treeview
        cat_columns = ('Category', 'Total Spent', 'Transaction Count', 'Average')
        self.cat_tree = ttk.Treeview(cat_frame, columns=cat_columns, show='headings', height=10)

        for col in cat_columns:
            self.cat_tree.heading(col, text=col)
            self.cat_tree.column(col, width=150)

        cat_scrollbar = ttk.Scrollbar(cat_frame, orient='vertical', command=self.cat_tree.yview)
        self.cat_tree.configure(yscrollcommand=cat_scrollbar.set)

        self.cat_tree.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        cat_scrollbar.pack(side='right', fill='y', pady=5)

        # Monthly trends frame
        monthly_frame = tk.LabelFrame(self.analysis_frame, text="Monthly Spending Trends",
                                      font=('Arial', 12, 'bold'), bg='white')
        monthly_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.monthly_text = tk.Text(monthly_frame, height=8, wrap='word',
                                    font=('Courier', 10), bg='#f8f9fa')
        self.monthly_text.pack(fill='both', expand=True, padx=5, pady=5)

    def refresh(self):
        # Update summary statistics
        total, count, avg = self.repo.get_summary_stats()
        self.total_label.config(text=f"${total:.2f}")
        self.count_label.config(text=str(count))
        self.avg_label.config(text=f"${avg:.2f}")

        # Update top category
        categories = self.repo.get_totals_by_category()
        if categories:
            top_category = categories[0][0]
            self.top_category_label.config(text=top_category)

        # Update insights
        self._update_insights(total, count, avg, categories)

        # Update recent expenses
        self._update_recent_expenses()

        # Update charts
        self._update_charts(categories)

        # Update analysis
        self._update_analysis()

    def _update_insights(self, total, count, avg, categories):
        self.insights_text.delete('1.0', 'end')

        insights = []

        if total > 0:
            insights.append(f"💡 Total spending of ${total:.2f} across {count} transactions")

            if avg > 100:
                insights.append("⚠️  High average expense - consider reviewing spending habits")

            if categories:
                top_pct = (categories[0][1] / total) * 100
                if top_pct > 40:
                    insights.append(f"📊 {categories[0][0]} represents {top_pct:.1f}% of total spending")

                insights.append(f"🏷️  Spending spread across {len(categories)} categories")

        # Add monthly trend insight
        monthly_data = self.repo.get_monthly_spending()
        if len(monthly_data) >= 2:
            current_month = monthly_data[0][1]
            previous_month = monthly_data[1][1]
            if previous_month > 0:
                change = ((current_month - previous_month) / previous_month) * 100
                if change > 0:
                    insights.append(f"📈 Spending increased by {change:.1f}% compared to last month")
                else:
                    insights.append(f"📉 Spending decreased by {abs(change):.1f}% compared to last month")

        insights_text = '\n'.join(insights) if insights else "📝 No expenses recorded yet"
        self.insights_text.insert('1.0', insights_text)

    def _update_recent_expenses(self):
        for row in self.recent_tree.get_children():
            self.recent_tree.delete(row)

        for date, cat, desc, amount in self.repo.get_recent_expenses(10):
            self.recent_tree.insert('', 'end', values=(date, cat, desc[:30] + '...' if len(desc) > 30 else desc,
                                                       f"${amount:.2f}"))

    def _update_charts(self, categories):
        # Clear all axes
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()

        # Chart 1: Category Pie Chart (Top 5 + Other)
        if categories:
            # Limit to top 5 categories, group rest into "Other"
            if len(categories) > 5:
                top_categories = categories[:5]
                other_total = sum(cat[1] for cat in categories[5:])
                cat_names = [cat[0] for cat in top_categories] + ['Other']
                cat_values = [cat[1] for cat in top_categories] + [other_total]
            else:
                cat_names = [cat[0] for cat in categories]
                cat_values = [cat[1] for cat in categories]

            self.ax1.pie(cat_values, labels=cat_names, autopct='%1.1f%%', startangle=90)
            self.ax1.set_title('Spending by Category', fontweight='bold')

        # Chart 2: Category Bar Chart
        if categories:
            cat_names = [cat[0] for cat in categories[:10]]  # Top 10
            cat_values = [cat[1] for cat in categories[:10]]

            bars = self.ax2.bar(cat_names, cat_values, color='skyblue')
            self.ax2.set_title('Top Spending Categories', fontweight='bold')
            self.ax2.set_xlabel('Category')
            self.ax2.set_ylabel('Amount ($)')
            self.ax2.tick_params(axis='x', rotation=45)

        # Chart 3: Monthly Trends (chronological order: oldest to newest)
        monthly_data = self.repo.get_monthly_spending()
        if monthly_data:
            # Reverse to get chronological order (oldest first)
            monthly_data_sorted = monthly_data[::-1]
            months = [m[0] for m in monthly_data_sorted]
            values = [m[1] for m in monthly_data_sorted]

            self.ax3.plot(months, values, marker='o', linewidth=2, markersize=6)
            self.ax3.set_title('Monthly Spending Trend', fontweight='bold')
            self.ax3.set_xlabel('Month')
            self.ax3.set_ylabel('Amount ($)')
            self.ax3.tick_params(axis='x', rotation=45)

        # Chart 4: Transaction Volume by Category
        cat_counts = self.repo.get_category_counts()
        if cat_counts:
            cat_names = [cat[0] for cat in cat_counts]
            cat_counts_values = [cat[1] for cat in cat_counts]

            self.ax4.bar(cat_names, cat_counts_values, color='lightcoral')
            self.ax4.set_title('Transaction Volume by Category', fontweight='bold')
            self.ax4.set_xlabel('Category')
            self.ax4.set_ylabel('Number of Transactions')
            self.ax4.tick_params(axis='x', rotation=45)

        self.fig.tight_layout(pad=2.0)
        self.canvas.draw()

    def _update_analysis(self):
        # Update category analysis
        for row in self.cat_tree.get_children():
            self.cat_tree.delete(row)

        categories = self.repo.get_totals_by_category()
        cat_counts = dict(self.repo.get_category_counts())

        for category, total in categories:
            count = cat_counts.get(category, 0)
            avg = total / count if count > 0 else 0
            self.cat_tree.insert('', 'end', values=(category, f"${total:.2f}", count, f"${avg:.2f}"))

        # Update monthly trends
        self.monthly_text.delete('1.0', 'end')
        monthly_data = self.repo.get_monthly_spending()

        if monthly_data:
            monthly_text = "Month      | Total Spent | Daily Average\n"
            monthly_text += "-" * 40 + "\n"

            for month, total in monthly_data[:12]:  # Last 12 months
                # Calculate days in month (simplified)
                try:
                    year, month_num = map(int, month.split('-'))
                    if month_num == 12:
                        next_month = datetime(year + 1, 1, 1)
                    else:
                        next_month = datetime(year, month_num + 1, 1)
                    current_month = datetime(year, month_num, 1)
                    days = (next_month - current_month).days
                    daily_avg = total / days if days > 0 else 0

                    monthly_text += f"{month} | ${total:9.2f} | ${daily_avg:9.2f}\n"
                except:
                    monthly_text += f"{month} | ${total:9.2f} | N/A\n"

            self.monthly_text.insert('1.0', monthly_text)
        else:
            self.monthly_text.insert('1.0', "No monthly data available")