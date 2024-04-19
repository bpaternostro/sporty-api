import React, { useEffect, useState } from 'react'
import { useGlobalContext } from '../../context/GlobalContextProvider'
import TableHeader from '../Table/TableHeader'
import TableRow from '../Table/TableRow'

import Widget from '../Widget/Widget'
import style from './dashboard.module.css'
import indexStyle from '../../style/index.module.css'
import buttonStyle from '../../style/buttons.module.css'

const Dashboard = () => {
    const {routines, customer} = useGlobalContext()
    const message = "No fue especificado"
    return (
        <div className={style.tableContainer}>
            {customer && 
            <div className={style.table}>
                <TableHeader></TableHeader>
                <div className={style.widgetContainer}>
                    <Widget name="Ult. entrenamiento" value={customer.kpis.last_training}></Widget>
                    <Widget name="Ult. 30 días entrenaste" value={customer.kpis.training_completed_in_last_30_days}></Widget>
                    <Widget name="Días sin entrenar" value={customer.kpis.ratio_hiking}></Widget>
                    <Widget name="Entrenamientos completados" value={customer.kpis.completed_training}></Widget>
                    <Widget name="Ratio bienestar" value={customer.kpis.ratio_welfare}></Widget>
                    <Widget name="Ratio esfuerzo" value={customer.kpis.ratio_effort}></Widget>
                    <Widget name="Ratio entretenimiento" value={customer.kpis.ratio_enjoyment}></Widget>
                </div>
                {routines.sort((a, b) => a.status_routine > b.status_routine ? 1 : -1).map( (t, i) => (
                    <TableRow routineData={t} key={i}></TableRow>
                ))}
            </div>}
        </div>
    )
}

export default Dashboard