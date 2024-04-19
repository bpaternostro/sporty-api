import React from 'react'
import styles from './table.module.css'

const TableHeader = () => {
  return (
    <div className={styles.tableHeader}>
        <h3 className={styles.tableHeaderTitle}>
            <span role="img" aria-label="waving-hand"> 👋 </span>
            <span className={styles.username}>{localStorage.getItem('name')}</span>
        </h3>
    </div>
  )
}

export default TableHeader